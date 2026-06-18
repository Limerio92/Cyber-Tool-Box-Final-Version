"""
Copyright© 29/04/2026, *****************************
Verison : 6.0
Projet - FIXED
"""

import paramiko
import csv

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

# Function to detect Active Directory service
def detect_active_directory(ip, username, password):
    # PowerShell command to check AD-related services
    command = "Get-Service -Name 'NTDS' | Select-Object Status,Name,DisplayName"
    result = execute_ssh_command(ip, username, password, command)
    
    if "Running" in result:
        return True
    
    return False

# Function to extract details from the AD tree
def extract_ad_tree(ip, username, password):
    # FIXED: Ask user for domain instead of using hardcoded value
    try:
        domain_input = input("Enter your AD domain (e.g., example.com or example.local): ").strip()
        
        if not domain_input:
            print("[-] Domain cannot be empty")
            return
        
        # Convert domain to DC format (example.com -> DC=example,DC=com)
        dc_parts = [f"DC={part}" for part in domain_input.split('.')]
        search_base = ','.join(dc_parts)
        
        # PowerShell command to get AD tree
        command = f"Get-ADObject -Filter * -SearchBase '{search_base}' -SearchScope Subtree | Format-Table -Wrap -AutoSize"
        result = execute_ssh_command(ip, username, password, command)
        
        csv_output_file = "ad_tree.csv"
        with open(csv_output_file, mode="w", newline='', encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Active Directory Tree"])
            
            for line in result.split("\n"):
                if line.strip():
                    csv_writer.writerow([line])
        
        print(f"[+] Active Directory tree has been saved to '{csv_output_file}'.")
    
    except Exception as e:
        print(f"[-] Error extracting AD tree: {e}")

# Example usage
def main():
    # Enter details of the remote machine
    ip = "192.168.1.100"
    username = "your_username"
    password = "your_password"
    
    # Check if Active Directory service is present
    ad_present = detect_active_directory(ip, username, password)
    
    if ad_present:
        print("Active Directory service detected.")
        # Extract AD tree
        extract_ad_tree(ip, username, password)
    else:
        print("Active Directory service not detected.")
