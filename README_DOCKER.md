# Audio2Hero Docker Quick Start

## Quick Setup for Unraid

1. **Copy files to Unraid:**
   ```bash
   # On your local machine, copy the audio2hero folder to Unraid
   scp -r audio2hero user@unraid-ip:/mnt/user/appdata/
   ```

2. **SSH into Unraid and create directories:**
   ```bash
   mkdir -p /mnt/user/appdata/audio2hero/{inputs,outputs,cache}
   cd /mnt/user/appdata/audio2hero
   ```

3. **Build and run:**
   ```bash
   docker-compose -f docker-compose.unraid.yml build
   docker-compose -f docker-compose.unraid.yml up -d
   ```

4. **Access the web interface:**
   - Open browser: `http://YOUR_UNRAID_IP:7860`
   - Upload audio files and download generated charts

## File Locations

- **Inputs:** `/mnt/user/appdata/audio2hero/inputs/`
- **Outputs:** `/mnt/user/appdata/audio2hero/outputs/`
- **Cache:** `/mnt/user/appdata/audio2hero/cache/` (model files)

## First Build Notes

- First build takes **15-30 minutes** (compiling essentia)
- Model download happens on first run (~500MB-1GB)
- Subsequent starts are much faster

## See Full Documentation

See `UNRAID_SETUP.md` for complete setup instructions and troubleshooting.

