# Sample code

This folder contains runnable examples for **PRIMER**, **MCP**, and a **Dummy IRCTC API** so you can compare the same use case (train status, PNR, train mapping) in both styles.

## Layout

```
code/
├── README.md           ← you are here
├── primer/             ← PRIMER: loop + your functions (no MCP)
├── mcp/                ← MCP: same capabilities as tools + resources
└── irctc-api/          ← Dummy IRCTC API (mock backend for trains/PNR)
```

## How to use

| Folder | What it is | When to use |
|--------|------------|-------------|
| **primer** | The PRIMER loop (prompt → reason → invoke → monitor → explain) with functions defined in your app. | When you don’t have an MCP setup; one app, one codebase. |
| **mcp** | An MCP server (and optional client) that exposes the same behaviour as **tools** (e.g. train status, PNR) and **resources** (e.g. train mapping). | When you want to use MCP clients (e.g. Cursor, Claude Desktop) with a standard protocol. |
| **irctc-api** | A dummy/mock API for train running status, PNR status, and train name→number mapping. | Shared backend for both PRIMER and MCP examples so they demonstrate the same domain. |

## Start everything (script)

From the **repo root**:

```bash
./scripts/start-all.sh
```

This starts the **IRCTC API** (background), **MCP Inspector** (background; open http://localhost:6274 to test the MCP server), and the **PRIMER** app (foreground). When you quit PRIMER (Ctrl+C or type `quit`), the API and Inspector are stopped. **Requires Node.js 20+** (MCP Inspector; use `nvm use` with `.nvmrc` if you use nvm).

**API only** (e.g. for MCP in Cursor):

```bash
./scripts/start-api-only.sh
```

**MCP Inspector** (test the MCP server in the browser):

```bash
./scripts/start-mcp-inspector.sh
```

Opens the Inspector at http://localhost:6274 and starts the IRCTC API if needed. Requires **Node.js 20+**.

## Run order (manual)

1. **Start the Dummy IRCTC API** (required for both PRIMER and MCP):
   ```bash
   cd code/irctc-api && uv run uvicorn main:app --reload
   ```
2. **PRIMER** (optional: set `OPENAI_API_KEY`):
   ```bash
   cd code/primer && uv run python app.py
   ```
3. **MCP** (for Cursor/Claude: run `uv run python server.py` from `code/mcp` and add as MCP server):
   ```bash
   cd code/mcp && uv run python server.py
   ```

## Full PRIMER implementation

The original PRIMER app (with in-process functions) lives in [YT-Assets AiAgent/code](https://github.com/shantanukhond/YT-Assets/tree/main/AiAgent/code). The `primer/` folder here is a **wrapper**: same loop, but tools call the dummy IRCTC API over HTTP.

## Quick links

- [PRIMER sample](./primer/) — PRIMER loop + HTTP client for irctc-api (uv).
- [MCP sample](./mcp/) — MCP server (FastMCP) with tools + resource calling irctc-api (uv).
- [Dummy IRCTC API](./irctc-api/) — mock API used by both samples.
