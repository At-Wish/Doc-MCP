# MCP sample (IRCTC API wrapper)

MCP server that exposes the same IRCTC capabilities as **tools** and a **resource** by calling the [Dummy IRCTC API](../irctc-api/). Any MCP client (e.g. Cursor, Claude Desktop) can then use train status, PNR, and train mapping over the protocol.

## Prerequisites

**IRCTC API running** (in another terminal):

```bash
cd code/irctc-api && uv run uvicorn main:app --reload
```

## Run with uv

From this folder (`code/mcp/`):

```bash
uv run python server.py
```

The server uses **stdio** transport by default (for Cursor / Claude Desktop). To use it in Cursor, add an MCP server entry that runs:

```bash
cd /path/to/Doc-MCP/code/mcp && uv run python server.py
```

## MCP Inspector (test tools & resources)

From the **repo root**, run:

```bash
./scripts/start-mcp-inspector.sh
```

This starts the [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) with this server and opens the UI (usually http://localhost:6274). You can try tools (`get_train_status_tool`, `get_pnr_status_tool`) and the resource (`irctc://train-mapping`) in the browser. The script starts the IRCTC API in the background if it isn’t already running. Requires **Node.js 20+** (MCP Inspector; see repo `.nvmrc`).

Optional env:

- `IRCTC_API_BASE_URL` — default `http://127.0.0.1:8000`

## What it exposes

| MCP concept | Name | Description |
|-------------|------|-------------|
| **Tool** | `get_train_status_tool` | Train running status (argument: `train_no`). Calls API `GET /train-status`. |
| **Tool** | `get_pnr_status_tool` | PNR ticket/seat status (argument: `pnr`). Calls API `GET /pnr`. |
| **Resource** | `irctc://train-mapping` | Train name → number list (read-only). Calls API `GET /train-mapping`. |

So the same backend (dummy IRCTC API) is used by both the **PRIMER** app (in-process loop + HTTP) and this **MCP** server (protocol tools + resource).
