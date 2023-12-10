# File handling capabilities to open and manipulate an existing file

# New .txt file
file_name = 'yeye.txt'

# Open the file in write mode to create it
with open(file_name, 'w') as file:
    # Write some lines to the file
    file.write("ASSSSSSSSSS.\n")
    file.write("Time or money?.\n")
    file.write("The answer may surprise you...\n")

# Open the file in read mode
with open(file_name, 'r') as file:
    # Read the first line and print it to the screen
    first_line = file.readline().strip()
    print("First line:", first_line)

# Delete the .txt file
import os
os.remove(file_name)