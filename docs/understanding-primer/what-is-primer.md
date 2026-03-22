---
sidebar_position: 2
---

# What is PRIMER?

PRIMER is a framework for building AI agents that follow a fixed loop: the user asks something, the AI reasons and plans, invokes a function, the app monitors the result, and the AI explains the answer (or the app recovers from an error). It was designed to work with the OpenAI API (e.g. GPT-4) and is extensible—you add new functions as needed.

:::tip When you don’t have a big MCP setup
You can use **PRIMER** when you don’t have (or need) a full MCP setup—no MCP servers, no MCP client, no protocol. Same loop: your app holds the prompt, calls your own functions (e.g. in a Python dict), and feeds results back to the model. **MCP** is for when you want that same loop standardized across many clients and servers; **PRIMER** is the lightweight version inside a single app.
:::

**Watch the PRIMER walkthrough:**

<iframe width="560" height="315" src="https://www.youtube.com/embed/W2ID_B7SXhw?si=qx6s4-MKDn12zRqt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## The six steps

| Letter | Step name       | What happens |
|--------|-----------------|--------------|
| **P**  | prompt_input    | User asks something. |
| **R**  | reason_plan     | AI reasons and decides what to do (e.g. which function to call). |
| **I**  | invoke_action   | The app calls the chosen function with the given input. |
| **M**  | monitor_result  | The app captures the function’s output and feeds it back. |
| **E**  | explain_output  | AI formats and returns the final answer to the user. |
| **R**  | recover_error   | If something fails, the app reports the error and the AI (or app) handles it. |

The loop runs until the AI returns an **explain_output** (success) or the flow stops after **recover_error**.

## The loop

1. User sends a request (**prompt_input**).
2. Model responds with a step (e.g. **reason_plan** or **invoke_action**).
3. If the step is **invoke_action**, the app runs the function and appends a **monitor_result** (or **recover_error**) to the conversation.
4. Model sees the result and either calls another tool, or returns **explain_output** and the loop ends.

Your app owns both the loop and the set of functions the model can call (e.g. get train status, get PNR status, get train number from name).

## The prompt

The model is given a system prompt that spells out the six steps and the available functions. It is asked to respond with JSON so the app can parse each step (e.g. `invoke_action` with a function name and input). Here is the prompt we used:

```text
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
3. getTrainNumberMapping() - Get train number from name.

Example:
START
{ "type": "prompt_input", "prompt": "get train running status for train 14682" }
{ "type": "reason_plan", "plan": "Call getTrainStatus for 14682" }
{ "type": "invoke_action", "function": "getTrainStatus", "input": "14682" }
{ "type": "monitor_result", "result": "Train is at NEW DELHI, delayed by 10 mins." }
{ "type": "explain_output", "response": "Train 14682 is at NEW DELHI, delayed by 10 minutes." }
```

## Example

For a query like *“get train running status for Karnataka Express”*:

- **reason_plan**: get the train number first, then get status.
- **invoke_action**: call something like `getTrainNumberMapping`, then `getTrainStatus` with that number.
- **monitor_result**: each function’s return value is fed back.
- **explain_output**: the model summarizes the answer for the user.

So PRIMER is a **structured agent loop** inside a single app: same steps every time, with your own functions and error handling.

The original write-up and code: [AiAgent – PRIMER with ChatGPT](https://github.com/shantanukhond/YT-Assets/tree/main/AiAgent). For MCP concepts, see [MCP Core Concept](/docs/mcp-core/overview).

Next: [How MCP is masked PRIMER](/docs/understanding-primer/how-mcp-is-primer) — prompt parts mapped to MCP, diagram, and implementation sketch.

