"""
Copyright© 29/04/2026, *****************************
Verison : 6.0
Projet
"""

# Import the search function from the googlesearch library
from googlesearch import search  

# Define a function to search for exploits related to a service
def search_exploit(service, html_render=False):

    # Create the search query by concatenating the service with the keywords "exploit vuln"
    query = service + " exploit vuln"
    
    # Perform the Google search with the specified query
    res = search(query, num_results=10, lang="en")

    # Initialize an empty string to store the information to display
    display_info = ""

    # Determine the spacing character based on HTML rendering
    spacing = "<br>" if html_render else "\n"

    # Initialize an empty list to store the links of search results
    links = []

    # Iterate through all search results
    for l in res:
        # Add each link to the list of links
        links.append(l)
    
    # Add header information if rendering is not HTML
    if not html_render:
        display_info += f"\n\n===================================\n"
        display_info += f" Exploits related to " + service
        display_info += f"\n===================================\n\n"

    # Iterate through all links in the list
    for link in links:
        # Add each link followed by the appropriate spacing to the display string
        display_info += f"{link}{spacing}"

    # Return the string containing the links of search results
    return display_info
