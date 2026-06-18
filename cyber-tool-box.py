"""
Copyright© 18/05/2026, *****************************
Verison : 6.0
Projet
"""

import os
from affichage_menu import Display_menu_title, Display_menu_options, Display_menu_optionScan, Display_menu_exploit, Display_menu_password, Display_menu_authentication, Display_menu_exploit_vuln, Display_menu_post_exploit
from colorama import init

# Import modules for different functionalities
# Scanning module
from modules.scan_ip_os import scan_addressing
from modules.portscan import Scan_Nmap, Scan_Nmap_Choice

# Vulnerability Detection module
from modules.searchsploit import search_exploit
from modules.scan_vulnerable_proto import scan_and_analyze_ports
from modules.scan_vulnerable_os import scan_and_analyze_os

# Security Analysis module
from modules.eval_password import evaluate_pwd_strength, evaluate_csv_passwords, add_line_to_csv_passwords

# Authentication Analysis module
from modules.Connection import ssh_connect_single, ssh_connect_multiple, http_connect_single, http_connect_multiple, add_line_csv_authen

# Vulnerability Exploitation module
from modules.keys_certif import scan_ssh_keys_windows, scan_ssh_keys_linux, scan_certificates_windows, scan_certificates_linux, detect_os

# Post Exploitation module
from modules.extract_ad import detect_active_directory, extract_ad_tree

# Report Creation module
from modules.gen_pdf import generate_security_report


if __name__ == "__main__":

    init()  # Initialize colorama for colored terminal output
    Display_menu_title()  # Display the menu title
    Display_menu_options()  # Display the main menu options
    
    option = int(input(">>> Choose an option\n>>> "))  # Read user's main menu choice

    while option != 99:  # Loop until the user chooses to exit

        if option == 1:  # If the user chooses Scanning
            Display_menu_optionScan()  # Display scanning submenu options
            subOption = str(input(">>> Choose an option\n>>> "))  # Read user's scanning submenu choice
            while subOption != 'z':  # Loop until the user chooses to go back

                if subOption == 'a':  # If the user chooses Network / OS Scan
                    try:
                        target_ip = input("Enter the IP address of the network to scan (ex: 192.168.1.0/24) : ")
                        if not target_ip.strip():
                            print("[-] IP address cannot be empty")
                        else:
                            scan_addressing(target_ip)
                    except Exception as e:
                        print(f"[-] Error during scan: {e}")

                if subOption == 'b':  # If the user chooses Port Scan
                    try:
                        TARGET = str(input(">>> Type target domain or IP\n>>> "))
                        scan, version = Scan_Nmap(TARGET)
                        print(scan)
                    except Exception as e:
                        print(f"[-] Error during port scan: {e}")

                if subOption == 'c':  # If the user chooses Custom Port Scan
                    try:
                        TARGET = str(input(">>> Type target domain or IP\n>>> "))
                        f_port = str(input(">>> The first port of range\n>>> "))
                        l_port = str(input(">>> The last port of range\n>>> "))
                        scan, version = Scan_Nmap_Choice(TARGET, f_port, l_port)
                        print(scan)
                    except Exception as e:
                        print(f"[-] Error during custom port scan: {e}")

                Display_menu_optionScan()  # Display scanning submenu options again
                subOption = str(input(">>> Choose an option\n>>> "))  # Read user's scanning submenu choice


        elif option == 2:  # If the user chooses Detection Vulnerabilities
            Display_menu_exploit()  # Display vulnerability detection submenu options
            subOption = str(input(">>> Choose an option\n>>> "))  # Read user's vulnerability detection submenu choice
            while subOption != 'z':  # Loop until the user chooses to go back

                if subOption == 'a':  # If the user chooses to search for vulnerabilities on a service
                    try:
                        service = str(input(">>> Search for exploits on a service (ex: wordpress 4.0)\n>>> "))
                        exploit = search_exploit(service)
                        print(exploit)
                    except Exception as e:
                        print(f"[-] Error searching exploits: {e}")

                if subOption == 'b':  # If the user chooses to search for vulnerabilities on a protocol
                    try:
                        ip_proto = str(input(">>> Choose the machine you want to scan (by IP)\n>>> "))
                        nb_ports_proto = str(input(">>> Choose the ports you want to scan (by ports, ex:1-50)\n>>> "))
                        result_vuln_proto = scan_and_analyze_ports(ip_proto, nb_ports_proto)
                        print(result_vuln_proto)
                    except Exception as e:
                        print(f"[-] Error scanning vulnerable protocols: {e}")

                if subOption == 'c':  # If the user chooses to search for vulnerabilities on an OS
                    try:
                        ip_os = str(input(">>> Choose the machine or range you want to scan (by IP or range, ex 192.168.1.1 or 192.168.1.1-50)\n>>> "))
                        result_vuln_os = scan_and_analyze_os(ip_os)
                        print(result_vuln_os)
                    except Exception as e:
                        print(f"[-] Error scanning vulnerable OS: {e}")

                
                Display_menu_exploit()  # Display vulnerability detection submenu options again
                subOption = str(input(">>> Choose an option\n>>> "))  # Read user's vulnerability detection submenu choice
        

        elif option == 3:  # If the user chooses Security Analysis
            Display_menu_password()  # Display password analysis submenu options
            subOption = str(input(">>> Choose an option\n>>> "))  # Read user's password analysis submenu choice
            while subOption != 'z':  # Loop until the user chooses to go back

                if subOption == 'a':  # If the user chooses to test a password
                    try:
                        password = input("Enter the password to test: ")
                        difficulty = evaluate_pwd_strength(password)
                        print("Password difficulty:", difficulty)
                    except Exception as e:
                        print(f"[-] Error evaluating password: {e}")

                if subOption == 'b':  # If the user chooses to test passwords from a CSV list
                    try:
                        csv_file_path = os.path.join("modules", "words_keys.csv")
                        results = evaluate_csv_passwords(csv_file_path)
                        for login, password, difficulty in results:
                            print(f"Login: {login}, Password: {password}, Difficulty: {difficulty}")
                    except FileNotFoundError:
                        print("[-] CSV file not found. Create modules/words_keys.csv first.")
                    except Exception as e:
                        print(f"[-] Error evaluating passwords: {e}")

                if subOption == 'c':  # If the user chooses to add a password to the CSV file
                    try:
                        new_username = input("Enter the new username/login : ")
                        new_password_pass = input("Enter the new password : ")
                        new_line_password = [new_username, new_password_pass]
                        name_file_csv = os.path.join("modules", "words_keys.csv")
                        add_line_to_csv_passwords(name_file_csv, new_line_password)
                        print("[+] Password added to CSV")
                    except Exception as e:
                        print(f"[-] Error adding password: {e}")
                    
                Display_menu_password()  # Display password analysis submenu options again
                subOption = str(input(">>> Choose an option\n>>> "))  # Read user's password analysis submenu choice


        elif option == 4:  # If the user chooses Authentication Password Analysis
            Display_menu_authentication()  # Display authentication analysis submenu options
            subOption = str(input(">>> Choose an option\n>>> "))  # Read user's authentication analysis submenu choice
            while subOption != 'z':  # Loop until the user chooses to go back

                if subOption == 'a':  # If the user chooses simple SSH authentication
                    try:
                        host_connection_ssh_s = input("Enter the IP of the machine you want to connect to: ")
                        login_connection_ssh_s = input("Enter the authentication login: ")
                        password_connection_ssh_s = input("Enter the authentication password: ")
                        ssh_connect_single(host_connection_ssh_s, login_connection_ssh_s, password_connection_ssh_s)
                    except Exception as e:
                        print(f"[-] SSH connection error: {e}")

                if subOption == 'b':  # If the user chooses multi-factor SSH authentication
                    try:
                        host_connection_ssh_m = input("Enter the IP of the machine you want to connect to: ")
                        file_authen = os.path.join("modules", "logins_authen.csv")
                        ssh_connect_multiple(host_connection_ssh_m, file_authen)
                    except FileNotFoundError:
                        print("[-] CSV file not found. Create modules/logins_authen.csv first.")
                    except Exception as e:
                        print(f"[-] SSH multi-auth error: {e}")

                if subOption == 'c':  # If the user chooses simple HTTP authentication
                    try:
                        url_connection_http_s = input("Enter the URL of the authentication page: ")
                        login_connection_http_s = input("Enter the authentication login: ")
                        password_connection_http_s = input("Enter the authentication password: ")
                        http_connect_single(url_connection_http_s, login_connection_http_s, password_connection_http_s)
                    except Exception as e:
                        print(f"[-] HTTP connection error: {e}")

                if subOption == 'd':  # If the user chooses multi-factor HTTP authentication
                    try:
                        url_connection_ssh_m = input("Enter the IP of the machine you want to connect to: ")
                        file_authen = os.path.join("modules", "logins_authen.csv")
                        http_connect_multiple(url_connection_ssh_m, file_authen)
                    except FileNotFoundError:
                        print("[-] CSV file not found. Create modules/logins_authen.csv first.")
                    except Exception as e:
                        print(f"[-] HTTP multi-auth error: {e}")
                
                if subOption == 'e':  # If the user chooses to add an authentication line to CSV
                    try:
                        new_login_authen = input("Enter the new login : ")
                        new_password_authen = input("Enter the new password : ")
                        new_line_authen = [new_login_authen, new_password_authen]
                        name_file2_csv = os.path.join("modules", "logins_authen.csv")
                        add_line_csv_authen(name_file2_csv, new_line_authen)
                        print("[+] Credentials added to CSV")
                    except Exception as e:
                        print(f"[-] Error adding credentials: {e}")
                    
                Display_menu_authentication()  # Display authentication analysis submenu options again
                subOption = str(input(">>> Choose an option\n>>> "))  # Read user's authentication analysis submenu choice


        elif option == 5:  # If the user chooses Exploitation of Vulnerabilities
            Display_menu_exploit_vuln()  # Display exploitation vulnerabilities submenu options
            subOption = str(input(">>> Choose an option\n>>> "))  # Read user's exploitation vulnerabilities submenu choice
            while subOption != 'z':  # Loop until the user chooses to go back

                if subOption == 'a':  # If the user chooses to retrieve authentication keys
                    try:
                        # Information about the remote machine
                        ip_exploit = input("Enter the IP of the machine you want to connect to: ")
                        username_exploit = input("Enter the authentication login: ")
                        password_exploit = input("Enter the authentication password: ")
                        
                        # Detect the type of operating system
                        os_type = detect_os(ip_exploit, username_exploit, password_exploit)
                        
                        print(f"The detected operating system is: {os_type}")
                        
                        # Execute operations according to the detected operating system
                        if os_type == "Windows":
                            scan_ssh_keys_windows(ip_exploit, username_exploit, password_exploit)

                        elif os_type == "Linux" or os_type == "macOS":
                            scan_ssh_keys_linux(ip_exploit, username_exploit, password_exploit)

                        else:
                            print("Unrecognized operating system. Unable to proceed.")
                    except Exception as e:
                        print(f"[-] Error retrieving SSH keys: {e}")

                if subOption == 'b':  # If the user chooses to retrieve certificates
                    try:
                        # Information about the remote machine
                        ip_exploit = input("Enter the IP of the machine you want to connect to: ")
                        username_exploit = input("Enter the authentication login: ")
                        password_exploit = input("Enter the authentication password: ")
                        
                        # Detect the type of operating system
                        os_type = detect_os(ip_exploit, username_exploit, password_exploit)
                        
                        print(f"The detected operating system is: {os_type}")
                        
                        # Execute operations according to the detected operating system
                        if os_type == "Windows":
                            scan_certificates_windows(ip_exploit, username_exploit, password_exploit)

                        elif os_type == "Linux" or os_type == "macOS":
                            scan_certificates_linux(ip_exploit, username_exploit, password_exploit)

                        else:
                            print("Unrecognized operating system. Unable to proceed.")
                    except Exception as e:
                        print(f"[-] Error retrieving certificates: {e}")
                    
                Display_menu_exploit_vuln()  # Display exploitation vulnerabilities submenu options again
                subOption = str(input(">>> Choose an option\n>>> "))  # Read user's exploitation vulnerabilities submenu choice


        elif option == 6:  # If the user chooses Post Exploitation
            Display_menu_post_exploit()  # Display post exploitation submenu options
            subOption = str(input(">>> Choose an option\n>>> "))  # Read user's post exploitation submenu choice
            while subOption != 'z':  # Loop until the user chooses to go back

                if subOption == 'a':  # If the user chooses to detect and extract Active Directory data
                    try:
                        # Information about the remote machine
                        ip_ad = input("Enter the IP of the machine you want to connect to: ")
                        username_ad = input("Enter the authentication login: ")
                        password_ad = input("Enter the authentication password: ")
                            
                        # Check if Active Directory service is present
                        ad_present = detect_active_directory(ip_ad, username_ad, password_ad)
                            
                        if ad_present:
                            print("Active Directory service detected.")
                            # Extract AD tree
                            extract_ad_tree(ip_ad, username_ad, password_ad)
                        else:
                            print("Active Directory service not detected.")
                    except Exception as e:
                        print(f"[-] Error with Active Directory: {e}")
                        
                Display_menu_post_exploit()  # Display post exploitation submenu options again
                subOption = str(input(">>> Choose an option\n>>> "))  # Read user's post exploitation submenu choice
        
        elif option == 7:  # If the user chooses Report Creation
            try:
                rapport_ip = input("Enter the IP address of the network to scan (ex: 192.168.1.0/24) : ")
                generate_security_report(rapport_ip)  # Generate the security report
            except Exception as e:
                print(f"[-] Error generating report: {e}")

        Display_menu_options()  # Display the main menu options again
        option = int(input(">>> Choose an option\n>>> "))  # Read user's main menu choice
