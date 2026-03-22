"""
MCP server: exposes IRCTC capabilities as tools and a resource by calling the dummy IRCTC API.
Run with: uv run python server.py (stdio) or use with Cursor/Claude Desktop.
"""
import json
import os

from mcp.server.fastmcp import FastMCP

from irctc_client import get_train_status, get_pnr_status, get_train_mapping

mcp = FastMCP(
    "IRCTC",
    description="Train status, PNR, and train name→number mapping via the dummy IRCTC API.",
)


@mcp.tool()
def get_train_status_tool(train_no: str) -> str:
    """Get live train running status for the given train number (e.g. 12627, 14682)."""
    try:
        data = get_train_status(train_no)
        return json.dumps(data, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
def get_pnr_status_tool(pnr: str) -> str:
    """Get PNR ticket and seat status for the given PNR number."""
    try:
        data = get_pnr_status(pnr)
        return json.dumps(data, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.resource("irctc://train-mapping")
def train_mapping_resource() -> str:
    """Train name → number mapping (read-only). Use to find train numbers by name."""
    try:
        data = get_train_mapping()
        return json.dumps(data, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def main():
    # stdio transport for Cursor / Claude Desktop
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
