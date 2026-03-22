# Dummy IRCTC API

A **mock IRCTC-style API** for train running status, PNR status, and train name→number mapping. Used by both the **PRIMER** and **MCP** samples so they demonstrate the same domain without a real IRCTC backend.

## Run with uv

From this folder (`code/irctc-api/`):

```bash
# Install deps and run the API (creates .venv if needed)
uv run uvicorn main:app --reload
```

API will be at **http://127.0.0.1:8000**. Docs at **http://127.0.0.1:8000/docs**.

### One-liner from repo root

```bash
cd code/irctc-api && uv run uvicorn main:app --reload
```

## Endpoints

| Capability           | Method | Example |
|----------------------|--------|---------|
| Train running status | `GET /train-status?train_no=12627` | Tool-like |
| PNR status           | `GET /pnr?pnr=1234567890`           | Tool-like |
| Train name → number  | `GET /train-mapping`               | Resource-like (read-only) |

## Examples

```bash
# Train status
curl "http://127.0.0.1:8000/train-status?train_no=12627"

# PNR
curl "http://127.0.0.1:8000/pnr?pnr=1234567890"

# Train mapping (list of trains)
curl "http://127.0.0.1:8000/train-mapping"
```

## Why “dummy”?

So the samples run without real IRCTC credentials or network. Same idea as in [YT-Assets AiAgent/code](https://github.com/shantanukhond/YT-Assets/tree/main/AiAgent/code) (e.g. `ntes_demo.py` with mock or local data).
