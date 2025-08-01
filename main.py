```python
import requests

def fetch_ip_info(ip_address):
    """
    Fetches information about a given IP address using the ip-api.com API.
    
    Args:
        ip_address (str): The IP address to look up.
        
    Returns:
        dict: The response containing geolocation and ISP information.
    """
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching IP information")
        return None

def display_ip_info(ip_info):
    """
    Displays formatted IP information to the console.
    
    Args:
        ip_info (dict): The IP information dictionary.
    """
    if ip_info:
        print(f"IP Address: {ip_info.get('query')}")
        print(f"Country: {ip_info.get('country')}")
        print(f"Region: {ip_info.get('regionName')}")
        print(f"City: {ip_info.get('city')}")
        print(f"ZIP: {ip_info.get('zip')}")
        print(f"ISP: {ip_info.get('isp')}")
        print(f"Latitude: {ip_info.get('lat')}")
        print(f"Longitude: {ip_info.get('lon')}")
    else:
        print("No information available.")

def main():
    """
    Main function to execute the IP lookup script.
    """
    ip_address = input("Enter an IP address to look up: ")
    ip_info = fetch_ip_info(ip_address)
    display_ip_info(ip_info)

if __name__ == "__main__":
    main()
```
