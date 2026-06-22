"""
Copyright© 29/04/2026, *****************************
Version : 6.0
Projet - FIXED
"""

import subprocess
import re
import scapy.all as scapy
from fpdf import FPDF, HTMLMixin
from datetime import datetime

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
    try:
        arp_request = scapy.ARP(pdst=ip_range)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        clients_list = [{"ip": element[1].psrc, "mac": element[1].hwsrc} for element in answered_list]
        return clients_list
    except:
        return []

class PDF(FPDF, HTMLMixin):
    def header(self):
        self.set_text_color(0, 0, 0)
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Network Security Report", 0, 1, "C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", 0, 0, "C")

def generate_security_report(network_range):
    import os
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    reports_dir = os.path.join(script_dir, "reports")
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    output_pdf = os.path.join(reports_dir, "Report_Security_Network_" + datetime.now().strftime('%Y-%m-%d_%H-%M') + ".pdf")

    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()

    HTML = ""
    HTML += "<p align='center'>------------------------------</p>"
    HTML += "<p align='center'>Analysis results</p>"
    HTML += "<p align='center'>------------------------------</p>"
    HTML += "<p></p>"
    HTML += "<p align='center'><i>This report aims to analyze and detect vulnerabilities in a private network.</i></p>"
    
    HTML += f"<p><b>Date:</b> {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>"
    HTML += f"<p><b>Target:</b> {network_range}</p>"

    print("=" * 60)
    print(f"[*] Analysis of network {network_range}")
    print("=" * 60)

    clients = scan_network(network_range)
    
    # Si ARP ne trouve rien, scanner l'IP directement
    if not clients:
        clients = [{"ip": network_range, "mac": "Unknown"}]

    HTML += "<p></p>"
    HTML += "<p align='center'><i>List of devices:</i></p>"
    HTML += "<table border='1' align='center'><tr><th>IP Address</th></tr>"

    for client in clients:
        ip_address = client["ip"]
        HTML += f"<tr><td>{ip_address}</td></tr>"

    HTML += "</table>"

    for client in clients:
        ip_address = client["ip"]
        HTML += f"<h3>Device: {ip_address}</h3>"
        print(f"[*] Analysis of device: {ip_address}")
        
        try:
            nmap_os_output = scan_os(ip_address)
            os_info = parse_nmap_os_output(nmap_os_output)
            insecure_os = check_os_versions(os_info)

            HTML += "<p><b>Operating System Information:</b></p><ul>"
            for info in os_info:
                HTML += f"<li>Operating System: {info['os']}</li>"
            HTML += "</ul>"

            if insecure_os:
                HTML += "<p><b>Insecure Operating Systems:</b></p><ul>"
                for os in insecure_os:
                    HTML += f"<li>Operating System: {os['os']}</li>"
                HTML += "</ul>"
        except Exception as e:
            print(f"[-] Error scanning OS: {e}")

        try:
            nmap_ports_output = scan_ports(ip_address)
            port_info = parse_nmap_output(nmap_ports_output)
            insecure_services = check_service_versions(port_info)

            HTML += "<p><b>Information on open ports:</b></p><ul>"
            for info in port_info:
                HTML += f"<li>Port: {info['port']}, Service: {info['service']}, Version: {info['version']}</li>"
            HTML += "</ul>"

            if insecure_services:
                HTML += "<p><b>Insecure Services or Versions Detected:</b></p><ul>"
                for svc in insecure_services:
                    HTML += f"<li>Port: {svc['port']}, Service: {svc['service']}, Version: {svc['version']}</li>"
                HTML += "</ul>"
        except Exception as e:
            print(f"[-] Error scanning ports: {e}")

        HTML += "<p>-----------------------------</p>"

    print("=" * 60)
    pdf.write_html(HTML)
    pdf.output(output_pdf)
    print(f"[+] Report generated: {output_pdf}")
    print("=" * 60)
