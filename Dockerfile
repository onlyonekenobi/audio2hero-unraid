FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies including FFmpeg and build tools for essentia
RUN apt-get update && apt-get install -y \
    ffmpeg \
    build-essential \
    cmake \
    libyaml-dev \
    libfftw3-dev \
    libavcodec-dev \
    libavformat-dev \
    libavutil-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
# Note: essentia will compile from source, this may take 10-15 minutes
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY *.py ./
COPY tokenizer.json ./

# Create directories for inputs and outputs
RUN mkdir -p /app/inputs /app/outputs

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV GRADIO_SERVER_NAME=0.0.0.0
ENV GRADIO_SERVER_PORT=7860

# Expose Gradio port
EXPOSE 7860

# Run the application
CMD ["python", "app.py"]

