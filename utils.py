import requests
import time
from config import ETHERSCAN_API_KEY

ETHERSCAN_API = "https://api.etherscan.io/api"

def get_transactions(address, start_block=0, end_block=99999999):
    url = (
        f"{ETHERSCAN_API}?module=account&action=txlist&address={address}"
        f"&startblock={start_block}&endblock={end_block}&sort=desc&apikey={ETHERSCAN_API_KEY}"
    )
    r = requests.get(url)
    data = r.json()
    if data["status"] != "1":
        print(f"⚠️ Etherscan error for {address}: {data['message']}")
        return []
    return data["result"]
