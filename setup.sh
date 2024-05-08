#!/bin/bash

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "Homebrew not found, installing now..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install system dependencies with Homebrew
brew install ghostscript tcl-tk

# Install Python dependencies with pip
pip install -r requirements.txt

echo "Setup completed!"