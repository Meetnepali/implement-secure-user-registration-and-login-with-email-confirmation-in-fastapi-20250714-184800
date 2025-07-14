#!/bin/bash
set -e
# Ensure dependencies are installed
if ! [ -d "venv" ]; then
  echo "Python virtual environment not found. Run install.sh first."
  exit 1
fi
source venv/bin/activate
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
