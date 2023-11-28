#!/bin/bash
#
# Manipulate a variable in bash to apply today’s date to a log file

# Set the source and destination file paths
# "." is current file path
source_file="/var/log/syslog"
destination_dir="."

# Get the current date and time
current_datetime=$(date "+%Y%m%d_%H%M%S")

# Create the destination filename with the appended date and time
destination_file="syslog_backup_${current_datetime}.log"

# Copy the source file to the destination directory with the new filename
cp "$source_file" "$destination_dir/$destination_file"

# Show on terminal the action completed
echo "Backup completed: $destination_dir/$destination_file"

# Delete the file afterwards (cleanup)
rm $destination_file