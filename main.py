```python
import requests
import json

def fetch_ip_info(ip_address):
    """
    Fetch information about a given IP address using the ipinfo.io API.
    
    Args:
        ip_address (str): The IP address to look up.
        
    Returns:
        dict: A dictionary containing the IP information or an error message.
    """
    try:
        # URL for the ipinfo.io API
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unable to fetch data for IP: {ip_address}"}
    except Exception as e:
        return {"error": str(e)}

def display_ip_info(ip_data):
    """
    Display the IP information in a user-friendly format.
    
    Args:
        ip_data (dict): The dictionary containing IP information.
    """
    if 'error' in ip_data:
        print(ip_data['error'])
    else:
        print(f"IP Address: {ip_data.get('ip', 'N/A')}")
        print(f"Hostname: {ip_data.get('hostname', 'N/A')}")
        print(f"City: {ip_data.get('city', 'N/A')}")
        print(f"Region: {ip_data.get('region', 'N/A')}")
        print(f"Country: {ip_data.get('country', 'N/A')}")
        print(f"Location: {ip_data.get('loc', 'N/A')}")
        print(f"Organization: {ip_data.get('org', 'N/A')}")

def main():
    """
    Main function to execute the script.
    """
    # Example IP address to lookup
    ip_address = input("Enter an IP address to look up: ")
    ip_info = fetch_ip_info(ip_address)
    display_ip_info(ip_info)

if __name__ == "__main__":
    main()
```