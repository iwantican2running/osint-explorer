```python
import requests
from bs4 import BeautifulSoup
import json

def fetch_ip_info(ip_address):
    """
    Fetches geolocation and other information about a given IP address.
    
    Args:
        ip_address (str): The IP address to query.
    
    Returns:
        dict: Parsed JSON response with IP information.
    """
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f"Error fetching data for IP {ip_address}: {response.status_code}")
        return {}

def scrape_web_page(url):
    """
    Scrapes a web page to extract all hyperlinks.
    
    Args:
        url (str): The URL of the web page to scrape.
    
    Returns:
        list: A list of hyperlinks found on the page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        return [a['href'] for a in soup.find_all('a', href=True)]
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return []

def main():
    # Example IP address to fetch information about
    ip_address = "8.8.8.8"
    ip_info = fetch_ip_info(ip_address)
    
    if ip_info:
        print("IP Information:", ip_info)

    # Example URL to scrape for hyperlinks
    url = "https://example.com"
    links = scrape_web_page(url)
    
    if links:
        print(f"Found {len(links)} links on {url}:")
        for link in links:
            print(link)

if __name__ == "__main__":
    main()
```
