import time
from config import WHALE_ADDRESSES, TX_THRESHOLD_ETH, CHECK_INTERVAL_SECONDS
from utils import get_transactions
from notify import send_alert

print("🐋 Whale Watcher started...")

last_seen = {}

while True:
    for address in WHALE_ADDRESSES:
        txs = get_transactions(address)
        if not txs:
            continue
        latest_tx = txs[0]
        tx_hash = latest_tx["hash"]
        if last_seen.get(address) == tx_hash:
            continue  # no new tx
        last_seen[address] = tx_hash

        value_eth = int(latest_tx["value"]) / 10**18
        if value_eth >= TX_THRESHOLD_ETH:
            send_alert(address, tx_hash, value_eth)

    time.sleep(CHECK_INTERVAL_SECONDS)
