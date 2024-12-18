#!/bin/bash

# Define the name of the virtual environment
VENV_DIR="venv"

# Check if the virtual environment already exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating a virtual environment..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
echo "Activating the virtual environment..."
source "$VENV_DIR/bin/activate"

# Install dependencies from requirements.txt
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Run the Python script (replace 'archive_log_files.py' with the actual script name)
echo "Running the Python script..."
python archive_log_files.py /path/to/logs # Adjust the folder path as needed

# Deactivate the virtual environment after execution
deactivate
