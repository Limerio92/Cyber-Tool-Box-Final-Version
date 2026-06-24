"""
Copyright© 29/04/2026, *****************************
Verison : 6.0
Projet
"""

import subprocess
import re
import scapy.all as scapy

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
def scan_addressing(target_ip):
    # Scanning the network to retrieve IP addresses of machines
    scanned_devices = scan(target_ip)

    if scanned_devices:
        print("\nScanning OS...")
        print(f"------------------------------------------------------------------")
        print("Detected Operating System Information:")

        for device in scanned_devices:
            ip_address = device["ip"]
            print(f"\nIP Address: {ip_address}")
            
            try:
                nmap_output = scan_os(ip_address)
                os_info = parse_nmap_os_output(nmap_output)
                
                if os_info:
                    for info in os_info:
                        print(f"Operating System: {info['os']} ")

                    insecure_os = check_os_versions(os_info)
                    if insecure_os:
                        print("\nInsecure Operating Systems Detected:")
                        for os in insecure_os:
                            print(f"Operating System: {os['os']}")

                else:
                    print("No operating system information detected.")
            except Exception as e:
                print(f"Error analyzing operating system for IP address {ip_address}: {e}")

    else:
        print("No devices found on the network.")
    print(f"------------------------------------------------------------------")
    print(f"")


# Function to scan the network and retrieve IP addresses
def scan(ip):
    # Sending an ARP request to obtain IP addresses in the specified network
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request

    # Selectionne automatiquement l'interface reliee au reseau cible
    target_prefix = ".".join(ip.split(".")[:3])
    selected_iface = None
    try:
        for iface in scapy.get_working_ifaces():
            if iface.ip and iface.ip.startswith(target_prefix):
                selected_iface = iface
                break
    except Exception:
        selected_iface = None

    if selected_iface:
        answered_list = scapy.srp(arp_request_broadcast, timeout=2,
                                  verbose=False, iface=selected_iface)[0]
    else:
        answered_list = scapy.srp(arp_request_broadcast, timeout=2,
                                  verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list
