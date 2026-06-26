"""
Cyber Tool Box v6.0 - Mr Robot Edition
fsociety inspired design
"""

# Importing datetime function from datetime module to get exact time of scan launch
from datetime import datetime
# Importing Nmap library to perform port scan
import nmap

# Function Scan_Nmap to perform port scan
def Scan_Nmap(ip):

    # Converting IP address to string
    ip = str(ip)

    # Initializing PortScanner object from Nmap library
    nm = nmap.PortScanner()
    displayInfo = ""

    # Displaying exact date and time of scan launch
    print(f"[+] Scan started at {datetime.now()}\n")

    # Scanning ports from 21 to 443 of specified IP address
    nm.scan(ip, '21-443')
    versions = []

    # Iterating through all hosts discovered by the scan
    for host in nm.all_hosts():

        # Adding host information to displayInfo string
        displayInfo += f"Host: {host} {nm[host].hostname()}\n"
        displayInfo += f"State: {nm[host].state()}\n"
        # Iterating through all protocols used by the host
        for proto in nm[host].all_protocols():

            displayInfo += f"---------------------\n"
            displayInfo += f"PORT\t\tSTATE\t\tPRODUCT\t\tVERSION\n"
            # Retrieving all ports used by the protocol
            lport = nm[host][proto].keys()

            # Iterating through all ports
            for port in lport:

                # Adjusting spacing for display
                if len(str(port) + str("/") + str(proto)) < 8:
                    space = "\t\t"
                else:
                    space = "\t"
                # Retrieving port information
                product = nm[host][proto][port]['product']
                version = nm[host][proto][port]['version']
                state = nm[host][proto][port]['state']

                # Adding port information to displayInfo string
                displayInfo += f"{port}/{proto}{space}{state}\t\t{product}\t\t{version}\n"
                # Adding product version to versions list
                if product != " " and product != "":
                    versions.append(product + " " + version)

            # Removing empty elements from versions list
            for v in versions:
                if v == '' or v == ' ':
                    versions.pop()

            # If no version is found, adding a message to versions list
            if len(versions) == 0:
                versions.append("No version found")

    # Returning host information and product versions
    return displayInfo, versions

def Scan_Nmap_Choice(ip, first_port=21, last_port=443):
    # Converting IP address to string
    ip = str(ip)

    # Initializing PortScanner object from Nmap library
    nm = nmap.PortScanner()
    displayInfo = ""

    # Displaying exact date and time of scan launch
    print(f"[+] Scan started at {datetime.now()}\n")

    # Constructing port range to scan
    port_range = f"{first_port}-{last_port}"

    # Scanning ports within specified range of IP address
    nm.scan(ip, port_range)
    versions = []

    # Iterating through all hosts discovered by the scan
    for host in nm.all_hosts():

        # Adding host information to displayInfo string
        displayInfo += f"Host: {host} {nm[host].hostname()}\n"
        displayInfo += f"State: {nm[host].state()}\n"
        # Iterating through all protocols used by the host
        for proto in nm[host].all_protocols():

            displayInfo += f"---------------------\n"
            displayInfo += f"PORT\t\tSTATE\t\tPRODUCT\t\tVERSION\n"
            # Retrieving all ports used by the protocol
            lport = nm[host][proto].keys()

            # Iterating through all ports
            for port in lport:

                # Adjusting spacing for display
                if len(str(port) + str("/") + str(proto)) < 8:
                    space = "\t\t"
                else:
                    space = "\t"
                # Retrieving port information
                product = nm[host][proto][port]['product']
                version = nm[host][proto][port]['version']
                state = nm[host][proto][port]['state']

                # Adding port information to displayInfo string
                displayInfo += f"{port}/{proto}{space}{state}\t\t{product}\t\t{version}\n"
                # Adding product version to versions list
                if product != " " and product != "":
                    versions.append(product + " " + version)

            # Removing empty elements from versions list
            for v in versions:
                if v == '' or v == ' ':
                    versions.pop()

            # If no version is found, adding a message to versions list
            if len(versions) == 0:
                versions.append("No version found")

    # Returning host information and product versions
    return displayInfo, versions
