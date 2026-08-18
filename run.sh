#!/usr/bin/env bash

set -e

VENV_DIR=".venv"
PYTHON_BIN="python3"
APP_FILE="app.py"
REQUIREMENTS_FILE="requirements.txt"

if ! command -v $PYTHON_BIN &> /dev/null; then
    echo "Python 3 is not installed or not on PATH."
    exit 1
fi

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    $PYTHON_BIN -m venv $VENV_DIR
fi

echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

echo "Upgrading pip..."
pip install --upgrade pip

if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r "$REQUIREMENTS_FILE"
else
    echo "requirements.txt not found. Installing known dependencies:"

    pip install \
        dash \
        dash-mantine-components \
        plotly
fi

echo "Please wait until you read 'Dash is running on http://127.0.0.1:8000/' before going to the link."
echo "The Bubble chart takes time to load. Refresh page if necessary."
python "$APP_FILE"
