#!/bin/bash

# Set the full path to your Python script. This is crucial for security.
PYTHON_SCRIPT="/Applications/Christmas Magsafe.app/Contents/Resources/main.py"

# Check if the script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
  echo "Error: Python script not found at $PYTHON_SCRIPT"
  exit 1
fi

# Run the Python script with sudo. Use the full path to python as well for extra safety
/usr/bin/sudo /usr/bin/python3 "$PYTHON_SCRIPT" # sudo is back here!!

# Check the exit code of the previous command
if [ $? -ne 0 ]; then
  echo "Error: Failed to run the Python script with sudo."
  exit 1
fi

echo "Python script executed successfully."
exit 0
