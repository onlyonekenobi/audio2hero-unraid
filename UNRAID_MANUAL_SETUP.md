# Unraid Manual Docker Setup (Without docker-compose)

If `docker-compose` is not available on your Unraid system, use these manual Docker commands.

## Step 1: Create Directories

```bash
mkdir -p /mnt/user/appdata/audio2hero/{inputs,outputs,cache}
cd /mnt/user/appdata/audio2hero
```

## Step 2: Build the Docker Image

```bash
docker build -t audio2hero:latest .
```

**Note:** This will take 15-30 minutes the first time as it compiles essentia from source.

## Step 3: Run the Container

```bash
docker run -d \
    --name audio2hero \
    --restart unless-stopped \
    -p 7860:7860 \
    -v /mnt/user/appdata/audio2hero/inputs:/app/inputs:ro \
    -v /mnt/user/appdata/audio2hero/outputs:/app/outputs \
    -v /mnt/user/appdata/audio2hero/cache:/root/.cache \
    -e PYTHONUNBUFFERED=1 \
    -e GRADIO_SERVER_NAME=0.0.0.0 \
    -e GRADIO_SERVER_PORT=7860 \
    -e OUTPUT_DIR=/app/outputs \
    --memory="8g" \
    --cpus="4" \
    audio2hero:latest
```

## Or Use the Helper Scripts

I've created helper scripts you can use:

```bash
# Make scripts executable
chmod +x build_docker.sh run_docker.sh

# Build the image
./build_docker.sh

# Run the container
./run_docker.sh
```

## Alternative: Try New Docker Compose Syntax

Some newer Unraid versions have `docker compose` (without the hyphen):

```bash
docker compose -f docker-compose.unraid.yml build
docker compose -f docker-compose.unraid.yml up -d
```

## Using Unraid Docker UI

You can also use the Unraid web interface:

1. **Go to Docker tab** in Unraid
2. **Click "Add Container"**
3. **Configure as follows:**

   **Basic Settings:**
   - **Name:** audio2hero
   - **Repository:** (leave blank - we'll use local image)
   
   **Advanced Settings:**
   - **Network Type:** Bridge
   - **Port Mappings:**
     - Container Port: `7860`
     - Host Port: `7860`
     - Protocol: `TCP`
   
   **Volume Mappings:**
   - `/mnt/user/appdata/audio2hero/inputs` → `/app/inputs` (read-only)
   - `/mnt/user/appdata/audio2hero/outputs` → `/app/outputs`
   - `/mnt/user/appdata/audio2hero/cache` → `/root/.cache`
   
   **Environment Variables:**
   - `PYTHONUNBUFFERED=1`
   - `GRADIO_SERVER_NAME=0.0.0.0`
   - `GRADIO_SERVER_PORT=7860`
   - `OUTPUT_DIR=/app/outputs`
   
   **Restart Policy:** Unless Stopped
   
   **Resource Limits:**
   - Memory: 8GB
   - CPUs: 4

4. **First, build the image via SSH:**
   ```bash
   cd /mnt/user/appdata/audio2hero
   docker build -t audio2hero:latest .
   ```

5. **Then in the UI, set Repository to:** `audio2hero:latest` (local image)

## Managing the Container

### View Logs
```bash
docker logs -f audio2hero
```

### Stop Container
```bash
docker stop audio2hero
```

### Start Container
```bash
docker start audio2hero
```

### Restart Container
```bash
docker restart audio2hero
```

### Remove Container (keeps volumes/data)
```bash
docker stop audio2hero
docker rm audio2hero
```

### Rebuild After Code Changes
```bash
docker stop audio2hero
docker rm audio2hero
docker build -t audio2hero:latest .
docker run -d --name audio2hero --restart unless-stopped \
    -p 7860:7860 \
    -v /mnt/user/appdata/audio2hero/inputs:/app/inputs:ro \
    -v /mnt/user/appdata/audio2hero/outputs:/app/outputs \
    -v /mnt/user/appdata/audio2hero/cache:/root/.cache \
    -e PYTHONUNBUFFERED=1 \
    -e GRADIO_SERVER_NAME=0.0.0.0 \
    -e GRADIO_SERVER_PORT=7860 \
    -e OUTPUT_DIR=/app/outputs \
    --memory="8g" --cpus="4" \
    audio2hero:latest
```

## Accessing the Application

Once running, access at:
```
http://YOUR_UNRAID_IP:7860
```

Replace `YOUR_UNRAID_IP` with your Unraid server's IP address.

