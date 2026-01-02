#!/bin/bash
# Audio2Hero WSL Run Script
# Run this script in WSL to start the application

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "Virtual environment not found. Run setup_wsl.sh first."
    exit 1
fi

# Run the application
echo "Starting Audio2Hero..."
python app.py
