---
sidebar_position: 1
---

# Introduction to MCP

This is not the official MCP documentation. It has been prepared as part of my personal exploration of the protocol, and I hope it makes MCP easier to grasp if you already think in terms of agent loops like PRIMER.

In the same way that **REST APIs** are a widely accepted way for frontends and backends to talk to each other, **Anthropic** introduced **MCP (Model Context Protocol)** as a standard way for AI applications to connect to external systems. For the official spec and getting started, see the [official MCP documentation](https://modelcontextprotocol.io/docs/getting-started/intro). If you notice anything off or missing here, feel free to open a pull request or reach out—thank you.

:::info Official definition
**MCP (Model Context Protocol)** is an open-source standard for connecting AI applications to external systems.

Using MCP, AI applications like Claude or ChatGPT can connect to data sources (e.g. local files, databases), tools (e.g. search engines, calculators) and workflows (e.g. specialized prompts)—enabling them to access key information and perform tasks.

Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems.
:::


To understand MCP we have two options 
1. You can go through MCP definition and theory
2. Understand MCP with single PRIMER prompt  

## Understanding MCP with single PRIMER prompt

1. **[What is PRIMER](/docs/understanding-primer/what-is-primer)** — The six steps, the prompt, and the loop.
2. **[How MCP is masked PRIMER](/docs/understanding-primer/how-mcp-is-primer)** — Prompt parts → MCP mapping, diagram, and implementation sketch.

## MCP Core Concept

**[MCP Core Concept](/docs/mcp-core/overview)** — Definition and theory (clients, servers, tools, resources).