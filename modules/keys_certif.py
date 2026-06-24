"""
Copyright© 29/04/2026, *****************************
Verison : 6.0
Projet
"""

import paramiko
import csv
import os

# Function to execute a command on a remote machine via SSH
def execute_ssh_command(ip, username, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(ip, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode("utf-8")
        error = stderr.read().decode("utf-8")
        
        if error:
            print(f"Error executing command: {error}")
        
        return output
    finally:
        client.close()


# Function to detect the operating system on the remote machine
def detect_os(ip, username, password):
    # Try to detect Linux or macOS
    command_uname = "uname -s"
    result = execute_ssh_command(ip, username, password, command_uname)
    
    if "Linux" in result:
        return "Linux"
    elif "Darwin" in result:
        return "macOS"
    
    # Try to detect Windows
    command_ver = "ver"
    result = execute_ssh_command(ip, username, password, command_ver)
    
    if "Microsoft" in result:
        return "Windows"
    
    return "Unknown"


# Function to scan SSH keys on Windows
def scan_ssh_keys_windows(ip, username, password):
    ssh_directory = f"C:\\Users\\{username}\\.ssh"
    command = f"dir {ssh_directory}"
    
    result = execute_ssh_command(ip, username, password, command)
    
    csv_output_file = "modules/ssh_keys_windows.csv"
    with open(csv_output_file, mode="w", newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["SSH File"])
        
        for line in result.split("\n"):
            if line.strip():  # Ignore empty lines
                csv_writer.writerow([line])
    
    print(f"Potential SSH keys on Windows have been saved in '{csv_output_file}'.")


# Function to scan SSH keys on Linux/macOS
def scan_ssh_keys_linux(ip, username, password):
    ssh_directory = "~/.ssh"
    command = f"ls -l {ssh_directory}"
    
    result = execute_ssh_command(ip, username, password, command)
    
    csv_output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ssh_keys_linux.csv")
    with open(csv_output_file, mode="w", newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["SSH File"])
        
        for line in result.split("\n"):
            if line.strip():  # Ignore empty lines
                csv_writer.writerow([line])
    
    print(f"Potential SSH keys on Linux/macOS have been saved in '{csv_output_file}'.")


# Function to scan personal certificates on Windows
def scan_certificates_windows(ip, username, password):
    command = "certutil -store my"
    
    result = execute_ssh_command(ip, username, password, command)
    
    csv_output_file = "modules/certificates_windows.csv"
    with open(csv_output_file, mode="w", newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Personal Certificates"])
        
        for line in result.split("\n"):
            if line.strip():  # Ignore empty lines
                csv_writer.writerow([line])
    
    print(f"Personal certificates on Windows have been saved in '{csv_output_file}'.")


# Function to scan personal certificates on Linux/macOS
def scan_certificates_linux(ip, username, password):
    command = "find /etc/ssl/certs -name '*.pem' -o -name '*.crt' 2>/dev/null"
    # For Linux, use appropriate commands
    
    result = execute_ssh_command(ip, username, password, command)
    
    csv_output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "certificates_linux.csv")
    with open(csv_output_file, mode="w", newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Personal Certificates"])
        
        for line in result.split("\n"):
            if line.strip():  # Ignore empty lines
                csv_writer.writerow([line])
    
    print(f"Personal certificates on Linux/macOS have been saved in '{csv_output_file}'.")
