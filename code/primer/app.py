"""
PRIMER app: same loop as YT-Assets (prompt → reason → invoke → monitor → explain),
but tools call the dummy IRCTC API instead of in-process functions.

Requires: IRCTC API running (cd code/irctc-api && uv run uvicorn main:app --reload).
Optional: OPENAI_API_KEY for the model (or set in .env).
"""
import json
import os
from openai import OpenAI

from irctc_client import get_train_status, get_pnr_status, get_train_number_mapping

SYSTEM_PROMPT = """
Follow the PRIMER steps to handle user requests using the available functions.

Steps:
- prompt_input: Wait for user input.
- reason_plan: Decide which function to call.
- invoke_action: Call the chosen function with input.
- monitor_result: Capture and observe the output.
- explain_output: Format and return the final answer.
- recover_error: Handle any issues and respond clearly.

Functions:
1. getTrainStatus(train_no: str) - Live train running status.
2. getPNRStatus(pnr: str) - PNR ticket & seat status.
3. getTrainNumberMapping() - Get train number from name (no input needed, pass "").

Example:
START
{ "type": "prompt_input", "prompt": "get train running status for train 14682" }
{ "type": "reason_plan", "plan": "Call getTrainStatus for 14682" }
{ "type": "invoke_action", "function": "getTrainStatus", "input": "14682" }
{ "type": "monitor_result", "result": "Train is at NEW DELHI, delayed by 10 mins." }
{ "type": "explain_output", "response": "Train 14682 is at NEW DELHI, delayed by 10 minutes." }
"""

TOOLS = {
    "getTrainStatus": get_train_status,
    "getPNRStatus": get_pnr_status,
    "getTrainNumberMapping": get_train_number_mapping,
}


def chat_with_gpt(messages: list[dict]) -> str:
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", ""))
    r = client.chat.completions.create(
        model=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
        messages=messages,
        temperature=0,
    )
    return r.choices[0].message.content or ""


def main():
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    print("PRIMER + IRCTC API. Say something (e.g. 'train status for 12627') or 'quit' to exit.\n")

    while True:
        query = input(">> ").strip()
        if not query or query.lower() in ("quit", "exit", "q"):
            break
        prompt_msg = {"type": "prompt_input", "prompt": query}
        messages.append({"role": "user", "content": json.dumps(prompt_msg)})

        while True:
            result = chat_with_gpt(messages)
            messages.append({"role": "assistant", "content": result})

            try:
                step = json.loads(result)
                print(f"🤖: {step}")

                if step.get("type") == "explain_output":
                    print(f"🤖: {step.get('response', '')}")
                    break

                if step.get("type") == "invoke_action":
                    fn_name = step.get("function", "")
                    fn_input = step.get("input", "") or ""
                    if fn_name not in TOOLS:
                        monitor_msg = {"type": "monitor_result", "result": f"Unknown function: {fn_name}"}
                    else:
                        try:
                            out = TOOLS[fn_name](fn_input)
                            monitor_msg = {"type": "monitor_result", "result": out}
                        except Exception as e:
                            monitor_msg = {"type": "recover_error", "error": str(e)}
                            messages.append({"role": "user", "content": json.dumps(monitor_msg)})
                            break
                    messages.append({"role": "user", "content": json.dumps(monitor_msg)})
                    continue

            except json.JSONDecodeError as e:
                print(f"⚠️ Invalid JSON from model: {e}")
                break


if __name__ == "__main__":
    main()
