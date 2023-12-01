#!/bin/bash
#
# Conditionals in Menu Systems

# The menu
while true; do
    # Display menu options
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"

    # Get user input
    read -p "Enter your choice (1-4): " choice

    # Evaluate user input
    # (Switch statements)
    case $choice in
        1)
            # Option: Hello world
            # ;; ends the switch statement and exits Switch completely
            # -e allows character escapes
            echo -e "\n\n\nRESULT:"
            echo -e "\nHello world!\n"
            ;;
        2)
            # Option: Ping self
            # echo is new line
            # -c control the number of pings to 4
            # IP address is localhost
            echo
            echo -e "\n\n\nRESULT:"
            ping -c 4 127.0.0.1
            echo
            ;;
        3)
            # Option: IP info
            echo
            echo -e "\n\n\nRESULT:"
            ifconfig
            echo
            ;;
        4)
            # Option: Exit
            # Exit script with success
            echo -e "\n\n\nExiting the menu"
            exit 0
            ;;
        *)
            # Invalid option
            echo -e "\n\n\nRESULT:"
            echo -e "\nPlease enter a number between 1 and 4\n"
            ;;
    esac

    # Add a newline for better readability in between
    echo
done