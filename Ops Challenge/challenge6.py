import os

# Declaration of functions

### Declare a function here
# file_content takes a path and tries to read all the files (including within
# directory)
def file_content(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        # Use os.walk() to get the list of files in the directory and its subdirectories
        for root, dirs, files in os.walk(file_path):
            for file_name in files:
                # Construct the full path to the file
                full_path = os.path.join(root, file_name)
                # Open and read the content of the file
                with open(full_path, 'r') as file:
                    file_content = file.read()
                    # If file is empty, print
                    if file_content == "":
                        print(f"\nFile {full_path} is empty")
                    else:
                        print(f"\nFile content of {full_path}:\n{file_content}")
        # If its not a file then
        else:
            print(f"{file_path} is a directory")
    else:
        print(f"{file_path} does not exist.")
#--------------------END FUNCTION------------------------------------------------
# Main

# Declaration of variables
# Ask the user for a file path
user_file_path = input("Enter file path: ")

### Pass the variable into the function here
file_content(user_file_path)

# End