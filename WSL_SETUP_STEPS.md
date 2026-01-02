# WSL Setup Steps for Audio2Hero

## Step-by-Step Instructions

Open **Ubuntu** (or your WSL terminal) and run these commands one by one. You'll see all output and can enter your password when prompted.

### Step 1: Navigate to the project
```bash
cd /mnt/c/Users/Luke/Documents/Cursor/audio2hero
```

### Step 2: Update system packages
```bash
sudo apt update
```
*(Enter your WSL password when prompted)*

### Step 3: Install required packages
```bash
sudo apt install -y python3 python3-pip python3-venv build-essential
```

### Step 4: Create virtual environment
```bash
python3 -m venv venv
```

### Step 5: Activate virtual environment
```bash
source venv/bin/activate
```
*(You should see `(venv)` in your prompt)*

### Step 6: Upgrade pip
```bash
pip install --upgrade pip
```

### Step 7: Install Python dependencies
```bash
pip install -r requirements.txt
```
*(This will take a few minutes - it needs to download and install packages including essentia)*

### Step 8: Run the application
```bash
python app.py
```

## Quick Setup (All at once)

If you prefer, you can run these commands in sequence:

```bash
cd /mnt/c/Users/Luke/Documents/Cursor/audio2hero
sudo apt update
sudo apt install -y python3 python3-pip python3-venv build-essential
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

## Troubleshooting

### If you get "command not found" errors:
- Make sure you're in the correct directory: `pwd` should show `/mnt/c/Users/Luke/Documents/Cursor/audio2hero`
- Check Python is installed: `python3 --version`

### If pip install fails:
- Make sure virtual environment is activated (you should see `(venv)` in prompt)
- Try: `pip install --upgrade pip` first
- Check internet connection in WSL

### If essentia installation fails:
- Make sure `build-essential` is installed: `sudo apt install build-essential`
- This is normal - essentia takes time to compile

## After Setup

Once everything is installed:
- The web interface will be available at `http://127.0.0.1:7860`
- You can access it from your Windows browser
- Generated files will be in the `Outputs` folder

