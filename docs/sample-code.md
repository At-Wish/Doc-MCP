---
sidebar_position: 2
---

# Sample code

We host sample code in this repo so you can see **how PRIMER used to work** and **how MCP works** for the same use case (train status, PNR, train mapping). A **Dummy IRCTC API** provides a shared mock backend for both.

## Repository layout

```
code/
├── primer/        → PRIMER: loop + your functions (no MCP)
├── mcp/            → MCP: same behaviour as tools + resources
└── irctc-api/      → Dummy IRCTC API (mock backend)
```

## What each folder is for

| Folder | Purpose |
|--------|--------|
| **[primer](https://github.com/At-Wish/Doc-MCP/tree/main/code/primer)** | PRIMER example: system prompt, tools dict, and the reason → invoke → monitor loop in one app. The full implementation lives in [YT-Assets AiAgent/code](https://github.com/shantanukhond/YT-Assets/tree/main/AiAgent/code); this folder links to it and can hold a minimal local example. |
| **[mcp](https://github.com/At-Wish/Doc-MCP/tree/main/code/mcp)** | MCP example: an MCP server that exposes the same capabilities as **tools** (e.g. getTrainStatus, getPNRStatus) and **resources** (e.g. train name→number mapping), so any MCP client can use them. |
| **[irctc-api](https://github.com/At-Wish/Doc-MCP/tree/main/code/irctc-api)** | Dummy IRCTC API: mock endpoints for train status, PNR, and train mapping. Both PRIMER and MCP samples can call it so you compare behaviour without a real IRCTC backend. |

## Compare PRIMER vs MCP

- **PRIMER:** One app, your functions, your loop. Good when you don’t have (or need) a full MCP setup. See [What is PRIMER](/docs/understanding-primer/what-is-primer).
- **MCP:** Same idea as a protocol: clients discover and call tools (and read resources) on servers. Good when you want many clients (e.g. Cursor, Claude Desktop) talking to many servers. See [How MCP is masked PRIMER](/docs/understanding-primer/how-mcp-is-primer).

The sample code shows both approaches over the same domain (trains/PNR) so you can switch from PRIMER to MCP when you’re ready.

## Testing the MCP server (MCP Inspector)

To test the MCP server (tools and resources) in the browser, run from the repo root:

```bash
./scripts/start-mcp-inspector.sh
```

This starts the [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) with our IRCTC MCP server and opens the UI (usually http://localhost:6274). The script starts the dummy IRCTC API in the background if needed. Requires **Node.js 20+** (MCP Inspector; see repo `.nvmrc`).

## Links

- **Code in this repo:** [Doc-MCP/code](https://github.com/At-Wish/Doc-MCP/tree/main/code)
- **Full PRIMER implementation:** [YT-Assets AiAgent/code](https://github.com/shantanukhond/YT-Assets/tree/main/AiAgent/code)
