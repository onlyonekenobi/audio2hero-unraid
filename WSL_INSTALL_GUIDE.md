# WSL Installation Guide for Audio2Hero

## Step-by-Step Installation

### Method 1: Using PowerShell (Recommended - Requires Admin)

1. **Open PowerShell as Administrator:**
   - Press `Windows Key + X`
   - Select "Windows PowerShell (Admin)" or "Terminal (Admin)"
   - Click "Yes" when prompted by User Account Control

2. **Run the installation command:**
   ```powershell
   wsl --install
   ```

3. **Restart your computer** when prompted (this is required)

4. **After restart**, WSL will finish installing and prompt you to create a Linux user account

### Method 2: Using Windows Features (Alternative)

1. **Open Windows Features:**
   - Press `Windows Key + R`
   - Type `optionalfeatures` and press Enter
   - Or search "Turn Windows features on or off" in Start menu

2. **Enable these features:**
   - ☑️ **Windows Subsystem for Linux**
   - ☑️ **Virtual Machine Platform** (if available)

3. **Click OK** and restart when prompted

4. **After restart**, open Microsoft Store and search for "Ubuntu" or "WSL"
   - Install "Ubuntu" (or "Ubuntu 22.04 LTS" recommended)

### Method 3: Manual Installation via Microsoft Store

1. **Open Microsoft Store**
2. **Search for "Ubuntu"** or "WSL"
3. **Install "Ubuntu"** (or "Ubuntu 22.04 LTS")
4. **Launch Ubuntu** from Start menu
5. **Create a username and password** when prompted

## After Installation

Once WSL is installed and you've restarted:

1. **Open Ubuntu** (or your chosen Linux distribution) from the Start menu
2. **Create your Linux username and password** (this is separate from your Windows password)
3. **Update the system:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

## Setting Up Audio2Hero in WSL

After WSL is installed, follow these steps:

1. **Navigate to your project in WSL:**
   ```bash
   cd /mnt/c/Users/Luke/Documents/Cursor/audio2hero
   ```

2. **Run the setup script:**
   ```bash
   bash setup_wsl.sh
   ```

   Or manually:
   ```bash
   # Install Python and dependencies
   sudo apt update
   sudo apt install -y python3 python3-pip python3-venv build-essential
   
   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate
   
   # Install Python dependencies
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

## Troubleshooting

### "WSL is not installed" error
- Make sure you restarted your computer after installation
- Try running: `wsl --install --distribution Ubuntu`

### "Virtual Machine Platform" error
- Enable "Virtual Machine Platform" in Windows Features
- Restart your computer

### Permission denied errors
- Make sure you're using `sudo` for system commands
- Check that your Linux user has proper permissions

### Can't access Windows files
- Windows drives are mounted at `/mnt/c/`, `/mnt/d/`, etc.
- Your C: drive is at `/mnt/c/`

## Quick Commands Reference

```bash
# Check WSL version
wsl --version

# List installed distributions
wsl --list --verbose

# Set default distribution
wsl --set-default Ubuntu

# Access WSL from Windows
wsl

# Exit WSL
exit
```

## Next Steps

Once WSL is installed and Audio2Hero is set up:
- The web interface will be available at `http://127.0.0.1:7860`
- You can access it from your Windows browser
- Files generated will be in the `Outputs` folder, accessible from both Windows and WSL




