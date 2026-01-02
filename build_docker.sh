#!/bin/bash
# Docker build script for Unraid (without docker-compose)

echo "Building Audio2Hero Docker image..."

# Build the image
docker build -t audio2hero:latest .

echo ""
echo "Build complete!"
echo ""
echo "To run the container, use:"
echo "  docker run -d \\"
echo "    --name audio2hero \\"
echo "    --restart unless-stopped \\"
echo "    -p 7860:7860 \\"
echo "    -v /mnt/user/appdata/audio2hero/inputs:/app/inputs:ro \\"
echo "    -v /mnt/user/appdata/audio2hero/outputs:/app/outputs \\"
echo "    -v /mnt/user/appdata/audio2hero/cache:/root/.cache \\"
echo "    -e PYTHONUNBUFFERED=1 \\"
echo "    -e GRADIO_SERVER_NAME=0.0.0.0 \\"
echo "    -e GRADIO_SERVER_PORT=7860 \\"
echo "    -e OUTPUT_DIR=/app/outputs \\"
echo "    audio2hero:latest"

