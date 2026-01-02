# Audio2Hero Docker Setup for Unraid

This guide will help you deploy Audio2Hero on your Unraid server using Docker.

## Prerequisites

- Unraid 6.9+ with Docker support
- At least 8GB RAM recommended (4GB minimum)
- Sufficient disk space for:
  - Docker image (~2-3GB)
  - Model files (~500MB-1GB cached)
  - Generated output files

## Method 1: Using Unraid Community Applications (Easiest)

### Step 1: Prepare Files on Unraid

1. **Create appdata directory structure:**
   ```bash
   mkdir -p /mnt/user/appdata/audio2hero/{inputs,outputs,cache}
   ```

2. **Copy the project files to Unraid:**
   - Copy the entire `audio2hero` folder to `/mnt/user/appdata/audio2hero/`
   - Or use SCP/SFTP to transfer files

### Step 2: Install via Docker Compose

1. **Install Docker Compose Manager** from Community Applications (if not already installed)

2. **Create a new stack:**
   - Go to Docker → Compose Manager
   - Click "Add New Stack"
   - Name it "audio2hero"
   - Point it to `/mnt/user/appdata/audio2hero/docker-compose.unraid.yml`
   - Click "Create Stack"

3. **Start the container:**
   - Click "Start" on the audio2hero stack
   - The first build will take 15-30 minutes (compiling essentia)

## Method 2: Manual Docker Setup

### Step 1: Prepare Directory Structure

SSH into your Unraid server and run:

```bash
# Create directories
mkdir -p /mnt/user/appdata/audio2hero/{inputs,outputs,cache}

# Navigate to appdata
cd /mnt/user/appdata/audio2hero
```

### Step 2: Copy Project Files

Copy all files from the audio2hero project to `/mnt/user/appdata/audio2hero/`:
- All `.py` files
- `requirements.txt`
- `tokenizer.json`
- `Dockerfile`
- `docker-compose.unraid.yml`

### Step 3: Build and Run

```bash
cd /mnt/user/appdata/audio2hero

# Build the Docker image (takes 15-30 minutes first time)
docker-compose -f docker-compose.unraid.yml build

# Start the container
docker-compose -f docker-compose.unraid.yml up -d

# View logs
docker-compose -f docker-compose.unraid.yml logs -f
```

## Method 3: Using Unraid Web UI

1. **Go to Docker tab** in Unraid
2. **Click "Add Container"**
3. **Configure:**
   - **Name:** audio2hero
   - **Repository:** (leave blank, we'll build locally)
   - **Build the image first:**
     ```bash
     cd /mnt/user/appdata/audio2hero
     docker build -t audio2hero .
     ```
   - **Port Mappings:**
     - Container Port: 7860
     - Host Port: 7860
   - **Volume Mappings:**
     - `/mnt/user/appdata/audio2hero/inputs` → `/app/inputs` (read-only)
     - `/mnt/user/appdata/audio2hero/outputs` → `/app/outputs`
     - `/mnt/user/appdata/audio2hero/cache` → `/root/.cache`
   - **Restart Policy:** Unless Stopped

## Accessing the Application

Once the container is running:

1. **Open your browser** and go to:
   ```
   http://YOUR_UNRAID_IP:7860
   ```
   Replace `YOUR_UNRAID_IP` with your Unraid server's IP address

2. **Upload an audio file** through the web interface

3. **Download the generated ZIP file** when processing completes

## File Management

### Input Files
- Place audio files in: `/mnt/user/appdata/audio2hero/inputs/`
- Or upload directly through the web interface

### Output Files
- Generated files are saved to: `/mnt/user/appdata/audio2hero/outputs/`
- Each song gets its own folder + a ZIP file

### Accessing Files from Windows
- Map a network drive to your Unraid shares
- Or use SMB share: `\\YOUR_UNRAID_IP\appdata\audio2hero\outputs`

## Troubleshooting

### Container won't start
```bash
# Check logs
docker logs audio2hero

# Check if port is already in use
netstat -tulpn | grep 7860
```

### Build fails on essentia
- Ensure you have enough disk space (at least 5GB free)
- The build can take 15-30 minutes, be patient
- Check logs: `docker-compose logs`

### Out of memory errors
- Reduce memory limits in `docker-compose.unraid.yml`
- Or add more RAM to your server

### Model download fails
- Check internet connection
- Ensure `/mnt/user/appdata/audio2hero/cache` has write permissions
- The model will cache in `/root/.cache` inside the container

### Can't access web interface
- Check firewall settings on Unraid
- Verify port 7860 is not blocked
- Check container logs: `docker logs audio2hero`

## Updating the Container

```bash
cd /mnt/user/appdata/audio2hero
docker-compose -f docker-compose.unraid.yml pull
docker-compose -f docker-compose.unraid.yml up -d --build
```

## Resource Usage

- **CPU:** 2-4 cores recommended during processing
- **RAM:** 4-8GB recommended
- **Disk:** ~5GB for image + cache + outputs
- **Processing Time:** 30-60 seconds per song (CPU) or 10-20 seconds (GPU if available)

## Optional: GPU Support

If you have an NVIDIA GPU and want to use it:

1. **Install NVIDIA Container Toolkit** on Unraid
2. **Add to docker-compose.unraid.yml:**
   ```yaml
   deploy:
     resources:
       reservations:
         devices:
           - driver: nvidia
             count: 1
             capabilities: [gpu]
   ```

## Maintenance

### View Logs
```bash
docker logs -f audio2hero
```

### Restart Container
```bash
docker restart audio2hero
```

### Stop Container
```bash
docker stop audio2hero
```

### Remove Container (keeps data)
```bash
docker stop audio2hero
docker rm audio2hero
```

