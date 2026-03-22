#!/usr/bin/env bash
# Start only the IRCTC API (e.g. for use with MCP in Cursor). Run from repo root: ./scripts/start-api-only.sh

set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/code/irctc-api"
echo "Starting IRCTC API at http://127.0.0.1:8000 (Ctrl+C to stop)"
exec uv run uvicorn main:app --reload --host 127.0.0.1 --port 8000
