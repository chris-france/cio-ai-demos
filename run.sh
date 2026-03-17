#!/bin/bash
# CIO AI Demos — React + FastAPI launcher
# Ctrl+C to stop

set -e
set -m

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Resolve symlinks to find the real script directory
SOURCE="${BASH_SOURCE[0]}"
while [ -L "$SOURCE" ]; do
    DIR="$(cd -P "$(dirname "$SOURCE")" && pwd)"
    SOURCE="$(readlink "$SOURCE")"
    [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
done
SCRIPT_DIR="$(cd -P "$(dirname "$SOURCE")" && pwd)"

BACKEND_PORT=18801
FRONTEND_PORT=18802
BACKEND_PID=""
FRONTEND_PID=""
HEADLESS=false
for arg in "$@"; do
    [ "$arg" = "--headless" ] && HEADLESS=true
done

cleanup() {
    echo ""
    echo -e "${YELLOW}→${NC} Shutting down..."

    # Kill tracked child processes
    [ -n "$BACKEND_PID" ] && kill "$BACKEND_PID" 2>/dev/null && wait "$BACKEND_PID" 2>/dev/null
    [ -n "$FRONTEND_PID" ] && kill "$FRONTEND_PID" 2>/dev/null && wait "$FRONTEND_PID" 2>/dev/null

    # Belt and suspenders — also kill anything still on the ports
    for PORT in $BACKEND_PORT $FRONTEND_PORT; do
        PIDS=$(lsof -ti :$PORT 2>/dev/null) || true
        [ -n "$PIDS" ] && echo "$PIDS" | xargs kill 2>/dev/null || true
    done

    echo -e "${GREEN}✓${NC} All processes stopped"
    exit 0
}
trap cleanup EXIT INT TERM

echo ""
echo "CIO AI Demos"
echo "============="
echo ""

# ---- Backend venv ----
if [ ! -d "$SCRIPT_DIR/backend/venv" ]; then
    echo -e "${YELLOW}→${NC} Creating backend virtual environment..."
    python3 -m venv "$SCRIPT_DIR/backend/venv"
    "$SCRIPT_DIR/backend/venv/bin/pip" install -q -r "$SCRIPT_DIR/backend/requirements.txt"
    echo -e "${GREEN}✓${NC} Backend venv ready"
else
    echo -e "${GREEN}✓${NC} Backend venv exists"
fi

# ---- Frontend deps ----
if [ ! -d "$SCRIPT_DIR/frontend/node_modules" ]; then
    echo -e "${YELLOW}→${NC} Installing frontend dependencies..."
    (cd "$SCRIPT_DIR/frontend" && npm install --silent)
    echo -e "${GREEN}✓${NC} Frontend deps ready"
else
    echo -e "${GREEN}✓${NC} Frontend deps exist"
fi

# ---- Start backend ----
echo -e "${YELLOW}→${NC} Starting backend on port $BACKEND_PORT..."
(cd "$SCRIPT_DIR/backend" && ./venv/bin/uvicorn main:app --host 0.0.0.0 --port $BACKEND_PORT --log-level warning) &
BACKEND_PID=$!

# Wait for backend
for i in $(seq 1 15); do
    curl -s "http://localhost:$BACKEND_PORT/api/demos" > /dev/null 2>&1 && break
    sleep 1
done
echo -e "${GREEN}✓${NC} Backend running on port $BACKEND_PORT (PID $BACKEND_PID)"

# ---- Start frontend ----
echo -e "${YELLOW}→${NC} Starting frontend on port $FRONTEND_PORT..."
(cd "$SCRIPT_DIR/frontend" && npx vite --port $FRONTEND_PORT --host 0.0.0.0) &
FRONTEND_PID=$!

# Wait for Vite
for i in $(seq 1 15); do
    curl -s "http://localhost:$FRONTEND_PORT" > /dev/null 2>&1 && break
    sleep 1
done
echo -e "${GREEN}✓${NC} Frontend running on port $FRONTEND_PORT (PID $FRONTEND_PID)"

echo ""
echo "CIO AI Demos running at http://localhost:$FRONTEND_PORT"
echo "Press Ctrl+C to stop"
echo ""

if [ "$HEADLESS" = false ]; then
    open "http://localhost:$FRONTEND_PORT"
fi

wait
