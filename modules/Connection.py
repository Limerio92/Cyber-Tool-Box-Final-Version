"""
Copyright© 29/04/2026, *****************************
Verison : 6.0
Projet
"""

import csv
import paramiko
import requests
from requests.auth import HTTPBasicAuth

def ssh_connect_single(hostname, username, password):
    """
    Connects to a machine via SSH with a single username/password pair.
    """
    # Create an SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Attempt to connect with the provided username and password
        ssh_client.connect(
            hostname, 
            username=username, 
            password=password,
            disabled_algorithms={'pubkeys': []},  # Accept old SSH keys
            look_for_keys=False,                   # Don't look for local keys
            allow_agent=False                      # Don't use SSH agent
        )
        print("[+] Connection successful")
        # Perform tasks here if connection is successful
        ssh_client.close()
        return True
    except paramiko.AuthenticationException:
        print("[-] Authentication failed")
        return False
    except Exception as e:
        print(f"[-] Error during connection: {e}")
        return False

def ssh_connect_multiple(hostname, filename):
    """
    Connects to a machine via SSH reading a CSV file of username/password pairs.
    """
    # Create an SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            
            for row in csv_reader:
                # Vérifie que la ligne contient bien login et mot de passe
                if len(row) == 2:
                    username = row[0]
                    password = row[1]
                    
                    try:
                        ssh_client.connect(
    hostname, 
    username=username, 
    password=password, 
    disabled_algorithms={'pubkeys': []}, # Autorise les vieilles clés (comme ssh-rsa)
    look_for_keys=False,                 # Ne cherche pas de clés locales (accélère le processus)
    allow_agent=False                    # N'utilise pas l'agent SSH de ton PC
)
                        print(f"[+] Connection successful with {username}/{password}")
                        ssh_client.close()
                        return True  # Stop if a connection is successful
                    except paramiko.AuthenticationException:
                        print(f"[-] Authentication failed with {username}/{password}")
                    except Exception as e:
                        print(f"[-] Error during connection with {username}/{password}: {e}")
                else:
                    print(f"[*] Ignored malformed line: {row}")
                    
    except FileNotFoundError:
        print(f"[-] Error: The file '{filename}' was not found.")

    return False  # Return False if no pair succeeded


def http_connect_single(url, username, password):
    """
    Connects to an HTTP service with a single username/password pair.
    """
    try:
        # Attempt to connect with the provided URL, username, and password
        response = requests.get(url, auth=HTTPBasicAuth(username, password))

        if response.status_code == 200:
            print("[+] Connection successful")
            return True
        else:
            print(f"[-] Connection failed with status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"[-] Error during connection: {e}")
        return False

def http_connect_multiple(url, filename):
    """
    Connects to an HTTP service reading a CSV file of username/password pairs.
    """
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            
            for row in csv_reader:
                if len(row) == 2:
                    username = row[0]
                    password = row[1]
                    
                    try:
                        # Attempt to connect with the provided URL, username, and password
                        response = requests.get(url, auth=HTTPBasicAuth(username, password))

                        if response.status_code == 200:
                            print(f"[+] Connection successful with {username}/{password}")
                            return True
                        else:
                            print(f"[-] Connection failed with {username}/{password}, status {response.status_code}")
                    except requests.exceptions.RequestException as e:
                        print(f"[-] Error during connection with {username}/{password}: {e}")
                else:
                    print(f"[*] Ignored malformed line: {row}")
                    
    except FileNotFoundError:
        print(f"[-] Error: The file '{filename}' was not found.")

    return False  # Return False if no pair succeeded


def add_line_csv_authen(filename, line):
    """
    Adds a new line to a CSV file.
    """
    # Open the CSV file in append mode and write the new line
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(line)
