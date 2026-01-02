#!/bin/bash
# Docker run script for Unraid (without docker-compose)

# Stop and remove existing container if it exists
docker stop audio2hero 2>/dev/null
docker rm audio2hero 2>/dev/null

echo "Starting Audio2Hero container..."

# Run the container
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

echo ""
echo "Container started!"
echo "Access the web interface at: http://YOUR_UNRAID_IP:7860"
echo ""
echo "To view logs: docker logs -f audio2hero"
echo "To stop: docker stop audio2hero"
echo "To restart: docker restart audio2hero"

