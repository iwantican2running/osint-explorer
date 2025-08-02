```python
import requests
from bs4 import BeautifulSoup

def get_ip_info(ip_address):
    """
    Fetches geographical and other information about a given IP address.
    
    Args:
        ip_address (str): The IP address to look up.

    Returns:
        dict: A dictionary containing the IP information.
    """
    url = f"https://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching IP info: {e}")
        return {}

def extract_emails_from_website(url):
    """
    Extracts email addresses from a given website URL.
    
    Args:
        url (str): The URL of the website to scrape.

    Returns:
        set: A set of unique email addresses found on the website.
    """
    email_set = set()
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all email addresses in the text of the website
        for word in soup.get_text().split():
            if "@" in word and "." in word:  # Basic email validation
                email_set.add(word.strip(",."))
    except requests.RequestException as e:
        print(f"Error fetching website: {e}")
    
    return email_set

if __name__ == "__main__":
    # Example usage
    ip = "8.8.8.8"
    website = "https://example.com"

    # Get IP information
    ip_info = get_ip_info(ip)
    if ip_info:
        print("IP Information:", ip_info)

    # Extract emails from the website
    emails = extract_emails_from_website(website)
    if emails:
        print("Emails found on the website:", emails)
    else:
        print("No emails found or an error occurred.")
```
