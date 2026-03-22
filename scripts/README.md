# Scripts

Run from the **repo root** (`Doc-MCP/`).

| Script | What it does |
|--------|----------------|
| **start-all.sh** | Starts **everything**: IRCTC API (background), MCP Inspector (background, opens http://localhost:6274), and PRIMER app (foreground). On exit (Ctrl+C or `quit`), stops the API and Inspector. Requires Node.js for the Inspector. |
| **start-api-only.sh** | Starts only the IRCTC API (useful when using the MCP server in Cursor/Claude). |
| **start-mcp-inspector.sh** | Runs only [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) with the IRCTC MCP server (starts the API if needed). Use when you don’t need PRIMER. |

Example (run everything):

```bash
./scripts/start-all.sh
```

Ensure `OPENAI_API_KEY` is set if you want the PRIMER model to respond.

## Node.js version

**Node.js 20+** is required for MCP Inspector (`npx @modelcontextprotocol/inspector`). If you see “Minimum Node.js version not met”, upgrade Node (e.g. `nvm install 20 && nvm use 20`, or install from [nodejs.org](https://nodejs.org/)). The repo includes a `.nvmrc` with `20`.
