"""
Cyber Tool Box v6.0 - Mr Robot Edition
fsociety inspired design
"""

import subprocess
import re

# List of secure and insecure operating systems
SECURE_OS_VERSIONS = {
    "windows": ["windows 10", "windows 11"],
    "linux": ["ubuntu 20.04", "ubuntu 22.04", "debian 10", "debian 11", "rhel 8", "centos 8"],
    "macos": ["macos monterey", "macos ventura"],
}

INSECURE_OS_VERSIONS = {
    "windows": ["windows xp", "windows vista", "windows 7"],
    "linux": ["ubuntu 18.04", "ubuntu 16.04", "debian 9", "centos 7"],
    "macos": ["macos mojave", "macos high sierra"],
}

# Function to execute an nmap scan with OS detection
def scan_os(ip_address):
    nmap_command = ["nmap", "-O", ip_address]
    result = subprocess.run(nmap_command, capture_output=True, text=True)

    if result.returncode != 0:
        raise Exception(f"Error executing nmap: {result.stderr}")

    return result.stdout


# Function to extract details about detected operating systems
def parse_nmap_os_output(nmap_output):
    os_info = []

    # Extracting OS details
    lines = nmap_output.split("\n")
    
    for line in lines:
        # Regex to extract OS details
        match = re.search(r"Running: (.+)", line)
        if match:
            os_description = match.group(1)

            os_info.append({"os": os_description})

    return os_info


# Function to check if operating system versions are secure
def check_os_versions(os_info):
    insecure_os = []

    for info in os_info:
        os_description = info["os"].lower()

        found_secure = False
        found_insecure = False

        for key, versions in SECURE_OS_VERSIONS.items():
            if any(secure in os_description for secure in versions):
                found_secure = True

        for key, versions in INSECURE_OS_VERSIONS.items():
            if any(insecure in os_description for insecure in versions):
                found_insecure = True

        if found_insecure and not found_secure:
            insecure_os.append(info)

    return insecure_os


# Main function to scan and analyze operating systems
def scan_and_analyze_os(target_ip):
    nmap_output = scan_os(target_ip)
    os_info = parse_nmap_os_output(nmap_output)
    

    if os_info:
        print()
        print(f"------------------------------------------------------------------")
        print("Detected Operating System Information:")
        for info in os_info:
            print(f"Operating System: {info['os']} ")

        insecure_os = check_os_versions(os_info)
        if insecure_os:
            print("\nInsecure Operating Systems Detected:")
            for os in insecure_os:
                print(f"Operating System: {os['os']}")
        else:
            print("\nAll operating systems appear to be secure.")
    else:
        print("No operating system information detected.")
    print(f"------------------------------------------------------------------")
