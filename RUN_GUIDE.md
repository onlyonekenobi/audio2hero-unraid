# Audio2Hero - Quick Start Guide

## ⚠️ Windows Users - Important!

If you're on Windows and getting an `essentia` import error, **please see [WINDOWS_SETUP.md](WINDOWS_SETUP.md)** for solutions. The `essentia` library cannot be installed on Windows with Python 3.12+.

**Quick options:**
- **Easiest**: Use the [HuggingFace Demo](https://huggingface.co/spaces/Tim-gubski/Audio2Hero) online
- **Best for local use**: Install WSL (Windows Subsystem for Linux) - see WINDOWS_SETUP.md
- **Alternative**: Use Python 3.11 or earlier

## Setup Complete! ✅

All dependencies have been installed (except `essentia` which cannot be installed on Windows with Python 3.12+).

## How to Run

### Option 1: Web Interface (Recommended)

Launch the Gradio web interface:

```bash
cd audio2hero
python app.py
```

This will start a web server. Open your browser to the URL shown (usually `http://127.0.0.1:7860`).

**Note:** The first time you run this, it will download the AI model from HuggingFace (several GB), which may take a few minutes.

### Option 2: Command Line

Run directly from command line:

```bash
cd audio2hero
python audio2hero.py "path/to/your/audio/file.mp3" "./Outputs"
```

**Important:** 
- Name your audio file as `Artist - Song Name.mp3` (e.g., `KISS - Rock & Roll All Nite.mp3`) for proper metadata extraction
- The output will be a ZIP file in the `Outputs` directory containing:
  - `notes.mid` - The generated MIDI chart
  - `song.ogg` - The audio file (converted to OGG)
  - `song.ini` - Metadata file for Clone Hero

## Output

The program generates:
- A ZIP file containing all necessary files for Clone Hero
- Medium difficulty chart (as per the model's current capabilities)
- Files ready to use in Clone Hero or edit in Moonscraper

## Known Limitations

- Only generates medium difficulty charts
- May sometimes follow other instruments (drums, bass, vocals) instead of just guitar
- Generated chart may sometimes exceed song duration
- May overlap sustained notes

## Troubleshooting

### Model Download Issues
If the model download fails, you may need to:
1. Check your internet connection
2. Ensure you have enough disk space (model is several GB)
3. Try running again - it will resume from where it left off

### Import Errors
If you get import errors, make sure you're in the `audio2hero` directory when running:
```bash
cd audio2hero
python app.py
```

### GPU Support
The program will automatically use GPU if available (CUDA), otherwise it will use CPU. CPU processing will be slower but still works.

