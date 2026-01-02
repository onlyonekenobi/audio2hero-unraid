#!/bin/bash
# Audio2Hero WSL Setup Script
# Run this script in WSL to set up the environment

echo "Setting up Audio2Hero in WSL..."

# Update package list
echo "Updating package list..."
sudo apt update

# Install Python and pip if not already installed
echo "Installing Python and dependencies..."
sudo apt install -y python3 python3-pip python3-venv build-essential

# Navigate to project directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "Setup complete! To run the application:"
echo "  1. Activate the virtual environment: source venv/bin/activate"
echo "  2. Run the app: python app.py"
echo ""
echo "Or run: bash run_wsl.sh"
