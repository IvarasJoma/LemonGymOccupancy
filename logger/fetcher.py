import requests
from config import URL

def fetch_html():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["content"]
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")