# How to Copy Text from WSL Terminal

## Method 1: Redirect Output to File (Easiest)

Run the app with output redirected to a file:

```bash
cd /mnt/c/Users/Luke/Documents/Cursor/audio2hero
source venv/bin/activate
python app.py > output.txt 2>&1
```

Then open `output.txt` from Windows (it's in the audio2hero folder) to copy the text.

## Method 2: Use the Capture Script

I've created a script that will save the output:

```bash
cd /mnt/c/Users/Luke/Documents/Cursor/audio2hero
bash capture_error.sh
```

This will save output to `error_output.txt` which you can open from Windows.

## Method 3: Copy from WSL Terminal

### Windows Terminal:
- Right-click in the terminal
- Select "Select All" or drag to select text
- Right-click again to copy (or Ctrl+Shift+C)

### Ubuntu Terminal:
- Click and drag to select text
- Right-click to copy
- Or use: Select text, then middle-click to paste

## Method 4: Describe the Error

If copying is too difficult, just describe:
- What command you ran
- What error message you saw (even if partial)
- At what step it failed

## Quick Commands to Get Error Info

Run these to get specific error information:

```bash
# Check Python version
python3 --version

# Check if packages are installed
pip list | grep -E "(essentia|transformers|torch)"

# Try importing to see specific error
python3 -c "import essentia"
python3 -c "from transformers import Pop2PianoProcessor"
```

