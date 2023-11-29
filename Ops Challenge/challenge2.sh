#!/bin/bash
#
# Alters file permissions of everything in a directory

# Prompt user for input directory path and store into the variable
read -p "Enter the directory path: " directory_path

# Check if the directory exists
# Error code 1 for error during execution of script
if [ ! -d "$directory_path" ]; then
    echo "Error: Directory not found."
    exit 1
fi

# Prompt user for input permissions number and store into variable
read -p "Enter the permissions number (e.g., 777): " permissions

# Change permissions of all files in the directory
# -R for recursive = apply to all sub directories and contents as well
chmod -R "$permissions" "$directory_path"

# Print directory contents and new permissions settings
# -e for backlashes to be escaped, \n = new line
echo -e "\nNew permissions:"
ls -l "$directory_path"

# Exit with success
exit 0