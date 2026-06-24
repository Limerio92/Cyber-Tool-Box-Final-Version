"""
Copyright© 29/04/2026, *****************************
Verison : 6.0
Projet
"""

import csv
import time
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
    Cree un nouveau client a chaque essai et gere proprement les deconnexions.
    """
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)

            for row in csv_reader:
                if len(row) == 2:
                    username = row[0]
                    password = row[1]

                    ssh_client = paramiko.SSHClient()
                    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                    try:
                        ssh_client.connect(
                            hostname,
                            username=username,
                            password=password,
                            disabled_algorithms={'pubkeys': []},
                            look_for_keys=False,
                            allow_agent=False,
                            timeout=5
                        )
                        print(f"[+] Connection successful with {username}/{password}")
                        ssh_client.close()
                        return True
                    except paramiko.AuthenticationException:
                        print(f"[-] Authentication failed with {username}/{password}")
                    except (paramiko.SSHException, ConnectionResetError, EOFError, OSError):
                        print(f"[-] Connection refused by server for {username}/{password} (rate-limit). Waiting...")
                        time.sleep(3)
                    except Exception as e:
                        print(f"[-] Error during connection with {username}/{password}: {e}")
                    finally:
                        ssh_client.close()

                    time.sleep(1)
                else:
                    print(f"[*] Ignored malformed line: {row}")

    except FileNotFoundError:
        print(f"[-] Error: The file '{filename}' was not found.")

    return False


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
    Adds a new line to a CSV file, ensuring it starts on a new line.
    """
    # Verifie si le fichier se termine deja par un saut de ligne
    needs_newline = False
    try:
        with open(filename, 'rb') as f:
            f.seek(0, 2)  # Va a la fin du fichier
            if f.tell() > 0:           # Fichier non vide
                f.seek(-1, 2)          # Dernier octet
                last_char = f.read(1)
                if last_char not in (b'\n', b'\r'):
                    needs_newline = True
    except FileNotFoundError:
        pass  # Le fichier sera cree

    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        if needs_newline:
            csvfile.write('\n')
        writer = csv.writer(csvfile)
        writer.writerow(line)
