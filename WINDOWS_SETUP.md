# Windows Setup Guide for Audio2Hero

## The Problem

The `essentia` library (required by `Pop2PianoProcessor`) cannot be installed on Windows with Python 3.12+ because:
1. It requires compilation from source
2. Its build system uses the `imp` module, which was removed in Python 3.12+
3. It's designed primarily for Linux/macOS

## Solutions

### Option 1: Use WSL (Windows Subsystem for Linux) - **RECOMMENDED**

WSL allows you to run Linux on Windows, where `essentia` can be installed easily.

#### Steps:
1. **Install WSL** (if not already installed):
   ```powershell
   wsl --install
   ```
   Restart your computer when prompted.

2. **Open WSL** and navigate to your project:
   ```bash
   # In WSL, mount your Windows drive and navigate
   cd /mnt/c/Users/Luke/Documents/Cursor/audio2hero
   ```

3. **Install Python and dependencies in WSL**:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   pip3 install -r requirements.txt
   ```

4. **Run the program in WSL**:
   ```bash
   python3 app.py
   ```

### Option 2: Use Docker

Create a Docker container with Linux to run the application.

#### Steps:
1. **Install Docker Desktop** from https://www.docker.com/products/docker-desktop

2. **Create a Dockerfile** (already provided if available, or create one)

3. **Build and run**:
   ```bash
   docker build -t audio2hero .
   docker run -p 7860:7860 audio2hero
   ```

### Option 3: Use Python 3.11 or Earlier

If you can use an older Python version, `essentia` might work.

#### Steps:
1. **Install Python 3.11** from https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"

2. **Create a virtual environment**:
   ```powershell
   py -3.11 -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run the program**:
   ```powershell
   python app.py
   ```

### Option 4: Use the HuggingFace Demo (Easiest)

The easiest solution is to use the online demo instead of running locally:
- Visit: https://huggingface.co/spaces/Tim-gubski/Audio2Hero
- Upload your audio file directly in the browser
- Download the generated ZIP file

## Recommendation

**For Windows users, I strongly recommend using WSL (Option 1)** as it:
- Provides the best compatibility
- Allows you to use the latest Python version
- Is the most reliable solution for this project
- Doesn't require managing multiple Python installations

## Quick WSL Setup Script

If you choose WSL, here's a quick setup script you can run in WSL:

```bash
#!/bin/bash
# Run this in WSL after installing WSL

# Update package list
sudo apt update

# Install Python and pip
sudo apt install -y python3 python3-pip python3-venv

# Navigate to project (adjust path as needed)
cd /mnt/c/Users/Luke/Documents/Cursor/audio2hero

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Save this as `setup_wsl.sh` and run: `bash setup_wsl.sh`




