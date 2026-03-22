# PRIMER sample (IRCTC API wrapper)

PRIMER loop (prompt → reason → invoke → monitor → explain) with **tools that call the [Dummy IRCTC API](../irctc-api/)**. Same behaviour as the [YT-Assets AiAgent](https://github.com/shantanukhond/YT-Assets/tree/main/AiAgent/code), but the backend is HTTP instead of in-process functions.

## Prerequisites

1. **IRCTC API running** (in another terminal):

   ```bash
   cd code/irctc-api && uv run uvicorn main:app --reload
   ```

2. **OpenAI API key** (for the model in the loop):

   ```bash
   export OPENAI_API_KEY=sk-...
   ```

## Run with uv

From this folder (`code/primer/`):

```bash
uv run python app.py
```

Or from repo root:

```bash
cd code/primer && uv run python app.py
```

Optional env vars:

- `IRCTC_API_BASE_URL` — default `http://127.0.0.1:8000`
- `OPENAI_MODEL` — default `gpt-4o-mini`

## What it does

- **Tools** (`irctc_client.py`): `getTrainStatus`, `getPNRStatus`, `getTrainNumberMapping` call the dummy API and return JSON strings.
- **Loop** (`app.py`): Same as YT-Assets: user input → model returns JSON step → if `invoke_action`, run tool (HTTP), append `monitor_result` → repeat until `explain_output`.

So PRIMER runs in one process and uses the IRCTC API as the backend; no MCP involved.
