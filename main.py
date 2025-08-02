```python
import requests
from bs4 import BeautifulSoup
import json

def fetch_ip_info(ip_address):
    """
    Fetches information about the given IP address using the ipinfo.io API.
    
    Args:
        ip_address (str): The IP address to look up.
        
    Returns:
        dict: Parsed JSON response containing IP information.
    """
    try:
        # API endpoint for fetching IP information
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Parse and return the JSON response
    except requests.RequestException as e:
        print(f"Error fetching data for IP {ip_address}: {e}")
        return None

def fetch_web_page(url):
    """
    Fetches the content of a web page and parses it for further analysis.
    
    Args:
        url (str): The URL of the web page to fetch.
        
    Returns:
        BeautifulSoup: Parsed HTML content of the web page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return BeautifulSoup(response.content, 'html.parser')
    except requests.RequestException as e:
        print(f"Error fetching page {url}: {e}")
        return None

def extract_links(soup):
    """
    Extracts and returns all hyperlinks from a BeautifulSoup object.
    
    Args:
        soup (BeautifulSoup): Parsed HTML of the web page.
        
    Returns:
        list: A list of hyperlinks found on the page.
    """
    return [a['href'] for a in soup.find_all('a', href=True)]

def main():
    ip_address = input("Enter an IP address to lookup: ")
    ip_info = fetch_ip_info(ip_address)
    
    if ip_info:
        print(json.dumps(ip_info, indent=4))  # Display IP information in a readable format
        
        # Optionally, fetch a web page related to the IP (e.g., a security blog)
        url = "https://example.com"  # Replace with a relevant URL
        soup = fetch_web_page(url)
        
        if soup:
            links = extract_links(soup)
            print("Extracted Links:")
            for link in links:
                print(link)

if __name__ == "__main__":
    main()
```

This Python script performs OSINT by fetching information about a given IP address and extracting links from a specified web page. It includes error handling and comments for clarity.