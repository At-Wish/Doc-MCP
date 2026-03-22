#!/usr/bin/env bash
# Run MCP Inspector with the IRCTC MCP server. Run from repo root: ./scripts/start-mcp-inspector.sh
# Inspector UI: http://localhost:6274 (see terminal for exact URL)
# Ensure IRCTC API is running first (./scripts/start-api-only.sh) so tools work.

set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# Start IRCTC API in background if not already up
API_PID=""
if ! curl -sf http://127.0.0.1:8000/ >/dev/null 2>&1; then
  echo "Starting IRCTC API in background (http://127.0.0.1:8000)..."
  cd "$ROOT/code/irctc-api"
  uv run uvicorn main:app --reload --host 127.0.0.1 --port 8000 &
  API_PID=$!
  cd "$ROOT"
  n=0
  until curl -sf http://127.0.0.1:8000/ >/dev/null 2>&1; do
    n=$((n + 1))
    [[ $n -ge 15 ]] && { echo "API did not start."; exit 1; }
    sleep 1
  done
  echo "IRCTC API is up."
fi

echo "Starting MCP Inspector (our server: code/mcp)..."
echo "Open the URL shown below (usually http://localhost:6274)"
echo ""

cleanup() {
  [[ -n "$API_PID" ]] && kill "$API_PID" 2>/dev/null || true
  exit 0
}
trap cleanup INT TERM

npx -y @modelcontextprotocol/inspector uv --directory "$ROOT/code/mcp" run python server.py
