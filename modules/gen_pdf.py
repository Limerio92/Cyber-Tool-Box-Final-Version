"""
Copyright© 29/04/2026, *****************************
Verison : 6.0
Projet
"""

import subprocess
import re
import scapy.all as scapy
import csv
import paramiko
import requests
from requests.auth import HTTPBasicAuth
from fpdf import FPDF
from fpdf import HTMLMixin
from datetime import datetime
from colorama import Fore, Back, Style, init

# Definitions of secure and insecure versions of operating systems and services
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

# Functions to perform scans and analyses
def scan_os(ip_address):
    nmap_command = ["nmap", "-O", ip_address]
    result = subprocess.run(nmap_command, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Error executing nmap: {result.stderr}")
    return result.stdout

def parse_nmap_os_output(nmap_output):
    os_info = []
    lines = nmap_output.split("\n")
    for line in lines:
        match = re.search(r"Running: (.+)", line)
        if match:
            os_description = match.group(1)
            os_info.append({"os": os_description})
    return os_info

def check_os_versions(os_info):
    insecure_os = []
    for info in os_info:
        os_description = info["os"].lower()
        found_secure = any(secure in os_description for versions in SECURE_OS_VERSIONS.values() for secure in versions)
        found_insecure = any(insecure in os_description for versions in INSECURE_OS_VERSIONS.values() for insecure in versions)
        if found_insecure and not found_secure:
            insecure_os.append(info)
    return insecure_os

def scan_ports(ip_address, ports="1-1024"):
    nmap_command = ["nmap", "-sV", "-p", ports, ip_address]
    result = subprocess.run(nmap_command, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Error executing nmap: {result.stderr}")
    return result.stdout

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

def check_service_versions(port_info):
    insecure_services = []
    for info in port_info:
        service = info["service"].lower()
        version = info["version"].lower()
        is_secure = any(secure_version in version for secure_version in SECURE_VERSIONS.get(service, []))
        is_insecure = any(insecure_version in version for insecure_version in INSECURE_VERSIONS.get(service, []))
        if is_insecure or not is_secure:
            insecure_services.append(info)
    return insecure_services

def scan_network(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = [{"ip": element[1].psrc, "mac": element[1].hwsrc} for element in answered_list]
    return clients_list

def ssh_connect_single(hostname, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(hostname, username=username, password=password)
        ssh_client.close()
        return True
    except paramiko.AuthenticationException:
        return False
    except Exception as e:
        print(f"Error connecting: {e}")
        return False

def http_connect_single(url, username, password):
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error connecting: {e}")
        return False


class PDF(FPDF, HTMLMixin):
    def header(self):
        self.set_text_color(255, 0, 0)  # Set text color to red
        self.set_font("Arial", "B", 20)  # Set font to Arial, bold, size 15
        self.cell(80)
        self.cell(30, 10, "Network Security Report", align="C")  # Customize the title
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)  # Set font to Arial, italic, size 8
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def header_html(self):
        self.set_y(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Network Security Report", 0, 1, "C")

def generate_security_report(network_range):
    output_pdf = "Report_Security_Network_" + datetime.now().strftime('%Y-%m-%d_%H-%M') + ".pdf"

    pdf = PDF()
    pdf.alias_nb_pages()  # Pour utiliser {nb} pour le nombre total de pages
    # pdf.add_page()

    HTML = ""
    HTML += "<p align='center'>------------------------------</p><ul>"
    HTML += "<p align='center'>Analysis results</p><ul>"
    HTML += "<p align='center'>------------------------------</p><ul>"
    HTML += "<p></p>"
    HTML += "<p align='center'><i>This report aims to analyze and detect vulnerabilities in a private network.</i></p>"
    
    HTML += f"<p><strong>Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>"
    HTML += f"<p><strong>Target:</strong> {network_range}</p>"

    print("--------------------------------------------------------")
    print(f">>> [*] Analysis of the network {network_range} / ...")
    print("--------------------------------------------------------")

    clients = scan_network(network_range)

    HTML += "<p></p>"
    HTML += "<p align='center'><i>List of devices:</i></p>"
    HTML += "<table border='1' align='center'><tr><th>IP Address</th></tr>"

    for client in clients:
        ip_address = client["ip"]
        HTML += f"<tr><td>{ip_address}</td></tr>"

    HTML += "</table>"
    pdf.add_page()

    for client in clients:
        ip_address = client["ip"]
        HTML += f"<h3 style='font-size: 15px;'>Device: {ip_address}</h3>"
        print(f"[*] Analysis of the device: {ip_address} / ...")
        
        nmap_os_output = scan_os(ip_address)
        os_info = parse_nmap_os_output(nmap_os_output)
        insecure_os = check_os_versions(os_info)

        HTML += "<p style='font-size: 5px;'><strong>Operating System Information:</strong></p><ul>"
        for info in os_info:
            HTML += f"<li style='font-size: 2px;'>Operating System: {info['os']}</li>"
        HTML += "</ul>"

        if insecure_os:
            HTML += "<p style='font-size: 5px;'><strong>Insecure Operating Systems:</strong></p><ul>"
            for os in insecure_os:
                HTML += f"<li style='font-size: 2px;'>Operating System: {os['os']}</li>"
            HTML += "</ul>"

        nmap_ports_output = scan_ports(ip_address)
        port_info = parse_nmap_output(nmap_ports_output)
        insecure_services = check_service_versions(port_info)

        HTML += "<p style='font-size: 5px;'><strong>Information on open ports:</strong></p><ul>"
        for info in port_info:
            HTML += f"<li style='font-size: 2px;'>Port: {info['port']}, Service: {info['service']}, Version: {info['version']}</li>"
        HTML += "</ul>"

        if insecure_services:
            HTML += "<p style='font-size: 5px;'><strong>Insecure Services or Versions Detected:</strong></p><ul>"
            for svc in insecure_services:
                HTML += f"<li style='font-size: 2px;'>Port: {svc['port']}, Service: {svc['service']}, Version: {svc['version']}</li>"
            HTML += "</ul>"

        HTML += "<p>-----------------------------</p>"

    print("--------------------------------------------------------")
    pdf.write_html(HTML)
    pdf.output(output_pdf)
