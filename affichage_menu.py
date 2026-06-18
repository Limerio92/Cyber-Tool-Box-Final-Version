"""

"""

from colorama import Fore, Back, Style

# Function to display the menu title
def Display_menu_title():
    displayInfo = rf"""{Fore.RED} 
___________           .__ __________              
\__    ___/___   ____ |  |\______   \ _______  ___
  |    | /  _ \ /  _ \|  | |    |  _//  _ \  \/  /
  |    |(  <_> |  <_> )  |_|    |   (  <_> >    < 
  |____| \____/ \____/|____/______  /\____/__/\_ \
                                  \/            \/

{Style.RESET_ALL}{Fore.YELLOW} ______  ______  _______ ______  ______  ______  ______  ______  ______ 
|______||______||_______|______||______||______||______||______||______|

{Style.RESET_ALL}{Fore.GREEN}______               ______              ___             ___
|  ___|              | ___ \             | |             | |            
| |_     ___   _ __  | |_/ /  ___  _ __  | |_   ___  ___ | |_           
|  _|   / _ \ | '__| |  __/  / _ \| '_ \ | __| / _ \/ __|| __|          
| |    | (_) || |    | |    |  __/| | | || |_ |  __/\__ \| |_           
\_|     \___/ |_|    \_|     \___||_| |_| \__| \___||___/ \__|   

{Style.RESET_ALL}{Fore.CYAN}
 version 6.0{Style.RESET_ALL}

 ************************************                                                                 
    """
    print(displayInfo)

# Function to display the main menu options
def Display_menu_options():
    # Construct the string for the main menu options
    displayInfo = f"""
    {Fore.GREEN}[ 1 ]{Style.RESET_ALL}  - Scanning 
    {Fore.GREEN}[ 2 ]{Style.RESET_ALL}  - Detection Vulnerabilities 
    {Fore.GREEN}[ 3 ]{Style.RESET_ALL}  - Security Analysis
    {Fore.GREEN}[ 4 ]{Style.RESET_ALL}  - Authentication Password Analysis
    {Fore.GREEN}[ 5 ]{Style.RESET_ALL}  - Exploitation of Vulnerabilities
    {Fore.GREEN}[ 6 ]{Style.RESET_ALL}  - Post Exploitation
    {Fore.GREEN}[ 7 ]{Style.RESET_ALL}  - Report Creation

    {Fore.YELLOW}[ 99 ]{Style.RESET_ALL} - Exit program
    """
    # Display the main menu options
    print(displayInfo)

# Function to display the scanning submenu options
def Display_menu_optionScan():
    # Construct the string for the scanning submenu options
    displayInfo = f"""
  {Fore.CYAN}[ 1 ] - Scanning{Style.RESET_ALL}

        {Fore.BLUE}[ a ]{Style.RESET_ALL} - Network / OS Scan
        {Fore.BLUE}[ b ]{Style.RESET_ALL} - Port Scan (21 - 433)
        {Fore.BLUE}[ c ]{Style.RESET_ALL} - Custom Port Scan
        
        {Fore.RED}z{Style.RESET_ALL} - Go back
  """
    # Display the scanning submenu options
    print(displayInfo)

# Function to display the vulnerabilities submenu options
def Display_menu_exploit():
    # Construct the string for the vulnerabilities submenu options
    displayInfo = f"""
  {Fore.CYAN}[ 2 ] - Vulnerabilities{Style.RESET_ALL}

        {Fore.BLUE}[ a ]{Style.RESET_ALL} - Search for vulnerabilities and exploits on a service
        {Fore.BLUE}[ b ]{Style.RESET_ALL} - Search for vulnerabilities on a protocol
        {Fore.BLUE}[ c ]{Style.RESET_ALL} - Search for vulnerabilities on an OS
        
        {Fore.RED}[ z ]{Style.RESET_ALL} - Go back
  """
    # Display the vulnerabilities submenu options
    print(displayInfo)

# Function to display the password testing submenu options
def Display_menu_password():
    # Construct the string for the password testing submenu options
    displayInfo = f"""
  {Fore.CYAN}[ 3 ] - Test Password{Style.RESET_ALL}

        {Fore.BLUE}[ a ]{Style.RESET_ALL} - Test password
        {Fore.BLUE}[ b ]{Style.RESET_ALL} - CSV password list
        {Fore.BLUE}[ c ]{Style.RESET_ALL} - Add line to CSV file

        {Fore.RED}[ z ]{Style.RESET_ALL} - Go back
 """
    # Display the password testing submenu options
    print(displayInfo)

# Function to display the authentication submenu options
def Display_menu_authentication():
    # Construct the string for the authentication submenu options
    displayInfo = f"""
  {Fore.CYAN}[ 4 ] - Authentication{Style.RESET_ALL}

        {Fore.BLUE}[ a ]{Style.RESET_ALL} - Simple SSH Authentication
        {Fore.BLUE}[ b ]{Style.RESET_ALL} - Multi-Factor SSH Authentication
        {Fore.BLUE}[ c ]{Style.RESET_ALL} - Simple HTTP Authentication
        {Fore.BLUE}[ d ]{Style.RESET_ALL} - Multi-Factor HTTP Authentication
        {Fore.BLUE}[ e ]{Style.RESET_ALL} - Add line to CSV file
        
        {Fore.RED}[ z ]{Style.RESET_ALL} - Go back
 """
    # Display the authentication submenu options
    print(displayInfo)

# Function to display the exploitation vulnerabilities submenu options
def Display_menu_exploit_vuln():
    # Construct the string for the exploitation vulnerabilities submenu options
    displayInfo = f"""
  {Fore.CYAN}[ 5 ] - Exploitation Vulnerabilities{Style.RESET_ALL}

        {Fore.BLUE}[ a ]{Style.RESET_ALL} - Retrieve authentication keys
        {Fore.BLUE}[ b ]{Style.RESET_ALL} - Retrieve certificates

        {Fore.RED}[ z ]{Style.RESET_ALL} - Go back
 """
    # Display the exploitation vulnerabilities submenu options
    print(displayInfo)

# Function to display the post exploitation submenu options
def Display_menu_post_exploit():
    # Construct the string for the post exploitation submenu options
    displayInfo = f"""
  {Fore.CYAN}[ 6 ] - Post Exploitation{Style.RESET_ALL}

        {Fore.BLUE}[ a ]{Style.RESET_ALL} - Detect an AD service and retrieve a CSV file of the domain's users and machine tree

        {Fore.RED}[ z ]{Style.RESET_ALL} - Go back
 """
    # Display the post exploitation submenu options
    print(displayInfo)
if __name__ == "__main__":
    Display_menu_title()
    Display_menu_options()