import psutil
import os
import time
import socket
from colorama import Fore, Style, init

# Initialize colorama for cross-platform color support
init(autoreset=True)

# Function to set the terminal window title
def set_terminal_title(title):
    if os.name == 'nt':  # Windows
        os.system(f'title {title}')
    else:  # Linux / macOS
        print(f"\033]0;{title}\007", end='')

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to list network interfaces and their details
def list_interfaces():
    try:
        interfaces = psutil.net_if_addrs()
        result = []
        for iface, addrs in interfaces.items():
            iface_details = f"Interface: {iface}\n"
            for addr in addrs:
                if addr.family == socket.AF_INET:  # IPv4 address
                    iface_details += f"  IPv4 Address: {addr.address}\n"
                    iface_details += f"  Netmask: {addr.netmask}\n"
                    iface_details += f"  Broadcast: {addr.broadcast}\n"
                elif addr.family == psutil.AF_LINK:  # MAC address
                    iface_details += f"  MAC Address: {addr.address}\n"
            result.append(iface_details)
        return result
    except Exception as e:
        print(Fore.RED + "Error fetching network addresses:", e)
        return []

# Function to simulate loading with a spinner
def loading_animation():
    for _ in range(3):
        for char in ['|', '/', '-', '\\']:
            print(Fore.GREEN + Style.BRIGHT + f"Loading {char}", end="\r")
            time.sleep(0.2)

# Function to print the title of the program
def print_title():
    clear_screen()  # Clear the screen every time the script runs
    set_terminal_title("NetScanner - Network Monitor")  # Set the custom terminal title
    print(Fore.CYAN + Style.BRIGHT + "==============================")
    print(Fore.GREEN + Style.BRIGHT + " NetScanner - Network Monitor")
    print(Fore.CYAN + Style.BRIGHT + "==============================\n")

# Function to display the available network interfaces and addresses
def print_interfaces(interfaces):
    if interfaces:
        print(Fore.YELLOW + Style.BRIGHT + "Available Network Interfaces and Details:\n")
        for i, info in enumerate(interfaces, 1):
            print(Fore.CYAN + f"{i}.\n{info}")
        print(Fore.YELLOW + "\nUse 'refresh' to reload or 'exit' to quit.")
    else:
        print(Fore.RED + "No network interfaces found.\n")

# Function to display developer info and credits
def print_developer_info():
    print(Fore.GREEN + "\n" + "=" * 55)
    print(Fore.MAGENTA + Style.BRIGHT + " Developed By ZoniBoy00 - https://github.com/ZoniBoy00")
    print(Fore.GREEN + "=" * 55)

# Main function to run the program
def main():
    loading_animation()  # Simulate loading animation before starting the main content
    print_title()
    interfaces = list_interfaces()
    print_interfaces(interfaces)
    print_developer_info()

    while True:
        command = input(Fore.MAGENTA + "\nEnter command (e.g., 'refresh' to refresh list or 'exit' to quit): ").strip().lower()
        
        if command == "exit":
            print(Fore.GREEN + "Exiting program...\n")
            break
        elif command == "refresh":
            loading_animation()  # Simulate loading animation when refreshing
            print_title()
            interfaces = list_interfaces()
            print_interfaces(interfaces)
        else:
            print(Fore.RED + "Unknown command. Please use 'refresh' or 'exit'.\n")

if __name__ == "__main__":
    main()
