#!/bin/bash
# Install FFmpeg in WSL

echo "Installing FFmpeg (required for audio processing)..."

# Update package list
sudo apt update

# Install FFmpeg
sudo apt install -y ffmpeg

# Verify installation
echo ""
echo "Verifying FFmpeg installation..."
ffmpeg -version
ffprobe -version

echo ""
echo "FFmpeg installed successfully!"

