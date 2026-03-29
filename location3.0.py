import requests
import subprocess
import time
from dotenv import load_dotenv
import os
load_dotenv()

wigle_password=os.getenv('WIGLE_API_KEY')

output=subprocess.run("netsh wlan show networks mode=bssid", capture_output=True)
output=str(output).split("\\n")
output.pop(0)
n=output[1][10]
l= {}
routers=[]
s=0
for i in output:
    if "BSSID" in i :
        l["bssid"]=i[i.index(":")+2:-3].strip()
    elif "Signal" in i:
        l["signal"]=int(i[i.index(":")+2:-5].strip())/2 -100
        routers.append(l)
        l={}


url = "https://api.wigle.net/api/v2/network/search"

headers = {
    "Accept": "application/json",
    "Authorization": f"Basic {wigle_password}"
}

for i in routers:
    TARGET_BSSID=i["bssid"]
    params = {
        "netid": TARGET_BSSID
    }

    print(f"Pinging WiGLE Global Database for {TARGET_BSSID}\n")

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()

            if data.get("success") and data.get("totalResults", 0) > 0:
                router_info = data["results"][0]

                lat = router_info.get("trilat")
                lon = router_info.get("trilong")
                road = router_info.get("road", "Unknown Street")
                city = router_info.get("city", "Unknown City")

                print("[SUCCESS] Router Found on the Grid! 🛰️")
                print("-" * 40)
                print(f"Latitude:  {lat}")
                print(f"Longitude: {lon}")
                print(f"Location:  {road}, {city}")

            else:
                print(
                    "[MISSING] Router not found. (If you just uploaded it, give the servers 24-48 hours to process your map data!)")

        elif response.status_code == 401:
            print("[ERROR 401] Unauthorized. Double-check your API key string!")
        elif response.status_code == 429:
            print("[ERROR 429] Too Many Requests. You hit the daily API limit.")
        else:
            print(f"[ERROR] Server responded with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

    time.sleep(2)