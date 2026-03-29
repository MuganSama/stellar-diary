import requests
import os
from dotenv import load_dotenv
load_dotenv()

wigle_password=os.getenv('WIGLE_API_KEY')

headers = {
    "Accept": "application/json",
    "Authorization": f"Basic {wigle_password}"
}

print("--- TEST 1: The Profile Check (Free Query) ---")
profile_url = "https://api.wigle.net/api/v2/profile/user"

try:
    profile_response = requests.get(profile_url, headers=headers)
    print(f"Status Code: {profile_response.status_code}")

    if profile_response.status_code == 200:
        data = profile_response.json()
        print("\n[SERVER RESPONSE DETECTED]")
        print(f"User: {data.get('userid')}")
        print(f"Queries Made Today: {data.get('queriesToday')}")
        print(f"Daily Limit: {data.get('queryLimitQ')}")
    else:
        print(f"Raw Error: {profile_response.text}")

except Exception as e:
    print(f"Connection failed: {e}")

print("\n--- TEST 2: The Single Router Ping ---")
# Testing just ONE single MAC address without loops
search_url = "https://api.wigle.net/api/v2/network/search"
params = {"netid": "c0:e6:24:fa:48:6e"}  # A random BSSID from your earlier scan

search_response = requests.get(search_url, headers=headers, params=params)
print(f"Search Status Code: {search_response.status_code}")
if search_response.status_code != 200:
    print(f"Raw Block Message: {search_response.text}")