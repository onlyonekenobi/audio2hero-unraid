#!/bin/bash
# Script to capture error output to a file

cd /mnt/c/Users/Luke/Documents/Cursor/audio2hero

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run app and capture all output (both stdout and stderr) to a file
python app.py 2>&1 | tee error_output.txt

echo ""
echo "Error output saved to: error_output.txt"
echo "You can now open this file from Windows to copy the text."

