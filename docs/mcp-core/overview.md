---
sidebar_position: 1
---

# MCP Core Concept

Short definitions of **tool**, **resource**, and **prompt** in MCP (and in this doc), and where they appear.

## What is a tool?

In MCP, a **tool** is an **action** the client can ask a server to run. The server advertises each tool with a name, description, and input parameters; the client invokes it with arguments and gets a result back.

- **Example:** `getTrainStatus(train_no)`, `getPNRStatus(pnr)` — the client calls them with inputs; the server runs them and returns output.
- **Where it’s mentioned in this doc:**  
  [Intro](/docs/intro) (official definition: “tools e.g. search engines, calculators”),  
  [How MCP is masked PRIMER](/docs/understanding-primer/how-mcp-is-primer) (table: “Functions” → MCP tools; invoke_action → client calls a tool; implementation sketch).

## What is a resource?

In MCP, a **resource** is **read-only data** the client can fetch by a URI. It is not an action to “invoke” — the client reads it (e.g. contents of a file, or a lookup like train name → number).

- **Example:** A train name → number mapping, or a file on disk. The client requests the resource by URI and gets back the data.
- **Where it’s mentioned in this doc:**  
  [How MCP is masked PRIMER](/docs/understanding-primer/how-mcp-is-primer) (table: getTrainNumberMapping → MCP resource; “read-only data the client fetches by URI”; implementation sketch).

## What is a prompt?

In this documentation we use **prompt** in two ways:

1. **PRIMER system prompt** — The text we give the model that lists the six steps (prompt_input, reason_plan, invoke_action, monitor_result, explain_output, recover_error) and the available functions. The model is instructed to respond with JSON for each step.  
   **Where it’s mentioned:**  
   [What is PRIMER](/docs/understanding-primer/what-is-primer) (“The prompt” section, full prompt in a code block),  
   [How MCP is masked PRIMER](/docs/understanding-primer/how-mcp-is-primer) (“Prompt with part-by-part mapping”, diagram).

2. **MCP / official docs** — The [official MCP definition](/docs/intro) says AI apps can connect to “workflows (e.g. specialized prompts)”. So in the broader MCP world, **prompts** can be part of workflows (e.g. reusable prompt templates). In our PRIMER→MCP mapping, the **prompt_input** step is the user’s message that the client receives, not an MCP “prompt” type by itself.

**Summary:** In our pages, “the prompt” usually means the **PRIMER system prompt**. “Tool” = action to invoke; “resource” = read-only data by URI; “prompt” = that system prompt or (in MCP) workflow-related prompts.
