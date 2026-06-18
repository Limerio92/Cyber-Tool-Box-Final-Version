"""
Copyright© 29/04/2026, *****************************
Verison : 6.0
Projet - FIXED
"""

import string
import csv
import os

def evaluate_pwd_strength(password):
    """Evaluates the strength of a password based on its length and complexity.

    Args:
        password (str): The password to evaluate.

    Returns:
        str: A message indicating the strength of the password.
    """
    length = len(password)
    strength = 0
    
    # Check for the presence of lowercase, uppercase, digits, and special characters
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1
    
    # Check if the password is common by comparing it to a list of common passwords
    common_pwd = False
    
    # FIXED: Use __file__ to find the logins file relative to this script
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        pwd_file = os.path.join(script_dir, 'logins')
        
        with open(pwd_file, 'r') as f:
            words = f.read().splitlines()
            if password.lower() in words:
                common_pwd = True
    except FileNotFoundError:
        print("[-] Warning: logins file not found. Skipping common password check.")
    except Exception as e:
        print(f"[-] Error reading logins file: {e}")

    score = length + strength
    
    # Evaluate the strength of the password based on the calculated score
    if common_pwd:
        return "Very Weak - Common password"
    elif score < 6:
        return "Very Weak"
    elif score < 10:
        return "Weak"
    elif score < 15:
        return "Average"
    elif score < 20:
        return "Good"
    else:
        return "Very Good"

def evaluate_csv_passwords(logins):
    """Evaluates the strength of passwords in a CSV file.

    Args:
        logins (str): The path to the CSV file containing usernames and passwords.

    Returns:
        list: A list of tuples containing the username, password, and its strength.
    """
    difficulties = []
    try:
        with open(logins, newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for line in csv_reader:
                if len(line) == 2:
                    username, password = line
                    difficulty = evaluate_pwd_strength(password)
                    difficulties.append((username, password, difficulty))
                else:
                    if line:  # Only print warning if line is not empty
                        print("The line does not contain two elements.")
    except FileNotFoundError:
        print(f"[-] CSV file not found: {logins}")
    except Exception as e:
        print(f"[-] Error reading CSV file: {e}")
    
    return difficulties

def add_line_to_csv_passwords(csv_file, line):
    """Adds a line to the CSV file containing usernames and passwords.

    Args:
        csv_file (str): The path to the CSV file.
        line (tuple): The tuple containing the username and password to add.
    """
    try:
        with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(line)
        print("[+] Password added successfully")
    except FileNotFoundError:
        print(f"[-] CSV file not found: {csv_file}")
    except Exception as e:
        print(f"[-] Error adding line to CSV: {e}")
