"""
Cyber Tool Box v6.0 - Mr Robot Edition
fsociety inspired design
"""

from colorama import Fore, Style, init
import re

init(autoreset=True)

G = Fore.LIGHTGREEN_EX
DG = Fore.GREEN
R = Fore.LIGHTRED_EX
W = Fore.LIGHTWHITE_EX
RS = Style.RESET_ALL

WIDTH = 60
BORDER = G + "+" + "-" * WIDTH + "+"

def vlen(s):
    """Visible length without ANSI codes"""
    return len(re.sub(r'\x1b\[[0-9;]*m', '', s))

def row(content):
    """Print a row with perfect border alignment"""
    pad = WIDTH - vlen(content)
    if pad < 0:
        pad = 0
    print(G + "|" + content + " " * pad + G + "|")

def empty():
    """Print empty bordered row"""
    print(G + "|" + " " * WIDTH + "|")

def display_menu_title():
    print("\n")
    print(G + "=" * (WIDTH + 2))
    row(W + " >>>>>> fsociety - CYBER TOOL BOX v6.0 <<<<<<".center(WIDTH))
    row(DG + " Hello, friend...".center(WIDTH))
    row(DG + " Are you ready to control the world?".center(WIDTH))
    print(G + "=" * (WIDTH + 2))
    print()

def display_menu_options():
    print(BORDER)
    row(W + " >> MAIN OPERATIONS // CHOOSE YOUR TARGET")
    print(BORDER)
    empty()
    row("  [" + W + "01" + G + "] " + W + "RECONNAISSANCE    " + DG + " :: Identify your target")
    row("  [" + W + "02" + G + "] " + W + "VULNERABILITIES   " + DG + " :: Find their weaknesses")
    row("  [" + W + "03" + G + "] " + W + "PASSWORD ATTACKS  " + DG + " :: Crack their defenses")
    row("  [" + W + "04" + G + "] " + W + "AUTHENTICATION    " + DG + " :: Bypass the gates")
    row("  [" + W + "05" + G + "] " + W + "EXPLOITATION      " + DG + " :: Extract their secrets")
    row("  [" + W + "06" + G + "] " + W + "POST-INFILTRATION " + DG + " :: Establish persistence")
    row("  [" + W + "07" + G + "] " + W + "GENERATE REPORT   " + DG + " :: Document the breach")
    empty()
    print(BORDER)
    row("  [" + R + "99" + G + "] " + W + "TERMINATE         " + DG + " :: Exit the session")
    print(BORDER)
    print()
    print(DG + "  > Control is an illusion.")
    print()

def display_menu_optionScan():
    print("\n")
    print(BORDER)
    row(W + " >> RECONNAISSANCE // GATHERING INTEL")
    print(BORDER)
    empty()
    row("  [" + W + "A" + G + "]  " + W + "Network Scan      " + DG + " :: Discover targets")
    row("  [" + W + "B" + G + "]  " + W + "Port Scan         " + DG + " :: Identify open services")
    row("  [" + W + "C" + G + "]  " + W + "Custom Range      " + DG + " :: Specific port targeting")
    empty()
    print(BORDER)
    row("  [" + R + "Z" + G + "]  " + W + "RETURN            " + DG + " :: Back to main menu")
    print(BORDER)
    print(DG + "  > The system is rigged. Time to expose it.")
    print()

def display_menu_exploit():
    print("\n")
    print(BORDER)
    row(W + " >> THREAT INTELLIGENCE // FIND THE GAPS")
    print(BORDER)
    empty()
    row("  [" + W + "A" + G + "]  " + W + "Search Exploits   " + DG + " :: Find known CVEs")
    row("  [" + W + "B" + G + "]  " + W + "Protocol Analysis " + DG + " :: Find weak protocols")
    row("  [" + W + "C" + G + "]  " + W + "OS Analysis       " + DG + " :: Find outdated systems")
    empty()
    print(BORDER)
    row("  [" + R + "Z" + G + "]  " + W + "RETURN            " + DG + " :: Back to main menu")
    print(BORDER)
    print(DG + "  > Everyone has weaknesses. Time to find them.")
    print()

def display_menu_password():
    print("\n")
    print(BORDER)
    row(W + " >> PASSWORD WARFARE // BREAK THE LOCKS")
    print(BORDER)
    empty()
    row("  [" + W + "A" + G + "]  " + W + "Test Single       " + DG + " :: Evaluate password")
    row("  [" + W + "B" + G + "]  " + W + "Bulk Analysis     " + DG + " :: Test from CSV file")
    row("  [" + W + "C" + G + "]  " + W + "Add to Vault      " + DG + " :: Save new credentials")
    empty()
    print(BORDER)
    row("  [" + R + "Z" + G + "]  " + W + "RETURN            " + DG + " :: Back to main menu")
    print(BORDER)
    print(DG + "  > Passwords are illusions. Time to shatter them.")
    print()

def display_menu_authentication():
    print("\n")
    print(BORDER)
    row(W + " >> ACCESS BREACH // BYPASS THE GATES")
    print(BORDER)
    empty()
    row("  [" + W + "A" + G + "]  " + W + "SSH Single        " + DG + " :: Test SSH credential")
    row("  [" + W + "B" + G + "]  " + W + "SSH Brute Force   " + DG + " :: Mass SSH attack")
    row("  [" + W + "C" + G + "]  " + W + "HTTP Single       " + DG + " :: Test HTTP credential")
    row("  [" + W + "D" + G + "]  " + W + "HTTP Brute Force  " + DG + " :: Mass HTTP attack")
    row("  [" + W + "E" + G + "]  " + W + "Add Credentials   " + DG + " :: Save to database")
    empty()
    print(BORDER)
    row("  [" + R + "Z" + G + "]  " + W + "RETURN            " + DG + " :: Back to main menu")
    print(BORDER)
    print(DG + "  > Authentication is the first lie.")
    print()

def display_menu_exploit_vuln():
    print("\n")
    print(BORDER)
    row(W + " >> EXTRACTION // GET WHAT'S YOURS")
    print(BORDER)
    empty()
    row("  [" + W + "A" + G + "]  " + W + "Extract SSH Keys  " + DG + " :: Get auth keys")
    row("  [" + W + "B" + G + "]  " + W + "Extract Certs     " + DG + " :: Harvest certificates")
    empty()
    print(BORDER)
    row("  [" + R + "Z" + G + "]  " + W + "RETURN            " + DG + " :: Back to main menu")
    print(BORDER)
    print(DG + "  > Steal what they hide. Expose what they fear.")
    print()

def display_menu_post_exploit():
    print("\n")
    print(BORDER)
    row(W + " >> DOMAIN CONTROL // OWN THE NETWORK")
    print(BORDER)
    empty()
    row("  [" + W + "A" + G + "]  " + W + "AD Enumeration    " + DG + " :: Extract domain info")
    empty()
    print(BORDER)
    row("  [" + R + "Z" + G + "]  " + W + "RETURN            " + DG + " :: Back to main menu")
    print(BORDER)
    print(DG + "  > Walk through their networks.")
    print()

# Legacy function names (used by cyber-tool-box.py)
def Display_menu_title():
    display_menu_title()

def Display_menu_options():
    display_menu_options()

def Display_menu_optionScan():
    display_menu_optionScan()

def Display_menu_exploit():
    display_menu_exploit()

def Display_menu_password():
    display_menu_password()

def Display_menu_authentication():
    display_menu_authentication()

def Display_menu_exploit_vuln():
    display_menu_exploit_vuln()

def Display_menu_post_exploit():
    display_menu_post_exploit()

if __name__ == "__main__":
    display_menu_title()
    display_menu_options()