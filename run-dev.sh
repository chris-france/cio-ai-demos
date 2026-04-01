#!/usr/bin/env bash
# Dev launcher — runs on different ports so it doesn't conflict with production
# Production: 18801 (backend) / 18802 (frontend)
# Dev:        18811 (backend) / 18812 (frontend)

set -e

SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "$0" 2>/dev/null || echo "$0")")" && pwd)"
cd "$SCRIPT_DIR"

BACKEND_PORT=18811
FRONTEND_PORT=18812

echo "=== CIO AI Demos — DEV MODE ==="
echo "Backend:  http://localhost:$BACKEND_PORT"
echo "Frontend: http://localhost:$FRONTEND_PORT"
echo ""

# Backend
cd backend
if [ ! -d venv ]; then
    python3 -m venv venv
    venv/bin/pip install -q -r requirements.txt 2>/dev/null || venv/bin/pip install fastapi uvicorn aiofiles openpyxl
fi
venv/bin/uvicorn main:app --host 0.0.0.0 --port $BACKEND_PORT &
BACKEND_PID=$!
cd ..

# Wait for backend
for i in $(seq 1 30); do
    curl -s "http://localhost:$BACKEND_PORT/api/demos" > /dev/null 2>&1 && break
    sleep 0.5
done

# Frontend (override proxy to point to dev backend)
cd frontend
npm install --silent 2>/dev/null
# Create temp vite config pointing to dev backend port
cat > vite.config.dev.js << VITEEOF
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    proxy: {
      '/api': 'http://localhost:$BACKEND_PORT',
    },
  },
})
VITEEOF
npx vite --config vite.config.dev.js --port $FRONTEND_PORT --host 0.0.0.0 &
FRONTEND_PID=$!
cd ..

# Wait for frontend
for i in $(seq 1 30); do
    curl -s "http://localhost:$FRONTEND_PORT" > /dev/null 2>&1 && break
    sleep 0.5
done

# Open browser
if [[ "$1" != "--headless" ]]; then
    open "http://localhost:$FRONTEND_PORT" 2>/dev/null || true
fi

echo ""
echo "Dev server running. Ctrl+C to stop."

cleanup() {
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}
trap cleanup INT TERM

wait
