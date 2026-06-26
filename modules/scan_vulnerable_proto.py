"""
Cyber Tool Box v6.0 - Mr Robot Edition
fsociety inspired design
"""

import subprocess
import re

# List of services with secure and insecure versions
SECURE_VERSIONS = {
    "ftp": ["ftps", "sftp"],
    "ssh": ["ssh-2"],
    "http": ["http/2", "http/1.1"],
    "https": ["tls 1.2", "tls 1.3"],
    "smtp": ["smtps", "smtp with starttls"],
    "imap": ["imap with starttls", "imap/ssl"],
    "pop3": ["pop3 with starttls", "pop3/ssl"],
    "rdp": ["rdp with nla"],
}

INSECURE_VERSIONS = {
    "ftp": ["ftp without encryption"],
    "ssh": ["ssh-1"],
    "http": ["http/1.0"],
    "https": ["ssl 3.0", "tls 1.0", "tls 1.1"],
    "smtp": ["smtp without encryption"],
    "imap": ["imap without encryption"],
    "pop3": ["pop3 without encryption"],
    "telnet": ["telnet"],
    "rdp": ["rdp without nla"],
}

# Function to execute an nmap scan and retrieve the result
def scan_ports(ip_address, ports="1-1024"):
    nmap_command = ["nmap", "-sV", "-p", ports, ip_address]
    result = subprocess.run(nmap_command, capture_output=True, text=True)

    if result.returncode != 0:
        raise Exception(f"Error executing nmap: {result.stderr}")

    return result.stdout


# Function to extract details of ports, services, and versions
def parse_nmap_output(nmap_output):
    port_info = []

    lines = nmap_output.split("\n")
    for line in lines:
        match = re.match(r"^(\d+/tcp)\s+open\s+(\w+)\s+(.*)", line)
        if match:
            port = match.group(1)
            service = match.group(2)
            version = match.group(3)
            port_info.append({"port": port, "service": service, "version": version})

    return port_info


# Function to check if service versions are secure
def check_service_versions(port_info):
    insecure_services = []

    for info in port_info:
        service = info["service"].lower()
        version = info["version"].lower()

        # Checking if the service version is not among the secure versions
        if service in SECURE_VERSIONS:
            is_secure = any(
                secure_version in version for secure_version in SECURE_VERSIONS[service]
            )
            if not is_secure:
                insecure_services.append(info)
        # Checking if the service version is among the insecure versions
        elif service in INSECURE_VERSIONS:
            is_insecure = any(
                insecure_version in version for insecure_version in INSECURE_VERSIONS[service]
            )
            if is_insecure:
                insecure_services.append(info)

    return insecure_services


# Main function to scan ports and check versions
def scan_and_analyze_ports(target_ip, ports="1-1024"):
    nmap_output = scan_ports(target_ip, ports)
    port_info = parse_nmap_output(nmap_output)

    print("Information on open ports:")
    for info in port_info:
        print(f"Port: {info['port']}, Service: {info['service']}, Version: {info['version']}")

    insecure_services = check_service_versions(port_info)
    if insecure_services:
        print("\nInsecure services or versions detected:")
        for svc in insecure_services:
            print(f"Port: {svc['port']}, Service: {svc['service']}, Version: {svc['version']}")
    else:
        print("\nAll services and versions appear to be secure.")
