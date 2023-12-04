# Use the module OS
import os


# Bash in Python

# Declare and initialize variables
name = "John Doe"
age = 25
city = "Dallas"

# Print the values of the variables
print("Name:", name)
print("Age:", age)
print("City:", city, "\n")

# Using module OS, BASH commands for the following
# print is used for new line spacing, easier readbility and see which command is
# being used
print("BASH command -> whoami:")
os.system("whoami")
print("\n\n\n")
print("BASH command -> ip a:")
os.system("ip a")
print("\n\n\n")
print("BASH command -> lshw -short")
os.system("lshw -short")
