import requests
import json

# Replace with your API key
API_KEY = 'YOUR API KEY HERE'

# Google Safe Browsing API endpoint
url = 'https://safebrowsing.googleapis.com/v4/threatMatches:find'

# Define the URL you want to check
def get_url_to_check():
    return input("Enter the URL you want to check: ")

# Create the request payload
def create_payload(url_to_check):
    return {
        "client": {
            "clientId": "your-app-name",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url_to_check}
            ]
        }
    }

# Send the POST request
def send_request(url, payload):
    try:
        response = requests.post(url, json=payload, params={'key': API_KEY})
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Handle the response
def handle_response(response):
    if response:
        data = response.json()
        if "matches" in data:
            print(f"The URL is potentially dangerous!")
            for match in data["matches"]:
                print(f"Threat type: {match['threatType']}")
        else:
            print(f"The URL appears to be safe.")

def main():
    url_to_check = get_url_to_check()
    payload = create_payload(url_to_check)
    response = send_request(url, payload)
    handle_response(response)

if __name__ == "__main__":
    main()
