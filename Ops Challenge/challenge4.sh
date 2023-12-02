#!/bin/bash
#
# Clearing Logs

# Define the log files
log_files=("/var/log/syslog" "/var/log/wtmp")

# Print original file sizes
echo "Original file sizes:"
for log_file in "${log_files[@]}"; do
    file_size=$(du -h "$log_file" | awk '{print $1}')
    echo "$log_file: $file_size"
done

# Set the backup directory
backup_dir="$HOME/backups"

# Ensure the backup directory exists
mkdir -p "$backup_dir"

# Get the current timestamp in YYYYMMDDHHMMSS
timestamp=$(date "+%Y%m%d%H%M%S")

# Compress and backup log files with gzip
# -c to send it to he compressed file variable
for log_file in "${log_files[@]}"; do
    compressed_file="$backup_dir/$(basename "$log_file")-$timestamp.zip"
    gzip -c "$log_file" > "$compressed_file"
    
    # Clear the contents of the log file
    > "$log_file"
    
    # Print compressed file size with command du
    #-h for human readable
    compressed_size=$(du -h "$compressed_file" | awk '{print $1}')
    echo "Compressed file size for $compressed_file: $compressed_size"
done

# Compare file sizes
#-e escape characters
echo -e "\nFile size comparison:"
for log_file in "${log_files[@]}"; do
    original_size=$(du -h "$log_file" | awk '{print $1}')
    compressed_file="$backup_dir/$(basename "$log_file")-$timestamp.zip"
    compressed_size=$(du -h "$compressed_file" | awk '{print $1}')
    
    echo "$log_file original size: $original_size"
    echo "$compressed_file compressed size: $compressed_size"
done

# Clean up
rm -r $backup_dir
exit 0