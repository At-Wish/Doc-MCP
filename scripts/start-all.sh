#!/usr/bin/env bash
# Start IRCTC API + MCP Inspector (browser) + PRIMER app. Run from repo root: ./scripts/start-all.sh
# On exit (Ctrl+C or quit PRIMER), API and Inspector are stopped.

set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

API_PID=""
INSPECTOR_PID=""
cleanup() {
  if [[ -n "$INSPECTOR_PID" ]] && kill -0 "$INSPECTOR_PID" 2>/dev/null; then
    echo "Stopping MCP Inspector (PID $INSPECTOR_PID)..."
    kill "$INSPECTOR_PID" 2>/dev/null || true
  fi
  if [[ -n "$API_PID" ]] && kill -0 "$API_PID" 2>/dev/null; then
    echo "Stopping IRCTC API (PID $API_PID)..."
    kill "$API_PID" 2>/dev/null || true
  fi
  exit 0
}
trap cleanup EXIT INT TERM

echo "Starting IRCTC API (http://127.0.0.1:8000)..."
cd "$ROOT/code/irctc-api"
uv run uvicorn main:app --reload --host 127.0.0.1 --port 8000 &
API_PID=$!
cd "$ROOT"

echo "Waiting for API to be ready..."
n=0
until curl -sf http://127.0.0.1:8000/ >/dev/null 2>&1; do
  n=$((n + 1))
  if [[ $n -ge 15 ]]; then
    echo "API did not start in time."
    exit 1
  fi
  sleep 1
done
echo "API is up."

echo "Starting MCP Inspector (http://localhost:6274)..."
npx -y @modelcontextprotocol/inspector uv --directory "$ROOT/code/mcp" run python server.py &
INSPECTOR_PID=$!
sleep 3
echo "Inspector should be open in your browser (or open http://localhost:6274)"
echo ""

echo "Starting PRIMER app (quit with Ctrl+C or type 'quit')..."
cd "$ROOT/code/primer"
uv run python app.py
