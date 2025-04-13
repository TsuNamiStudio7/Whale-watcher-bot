def send_alert(address, tx_hash, amount_eth):
    print("🚨 Whale Alert!")
    print(f"Wallet: {address}")
    print(f"Tx: https://etherscan.io/tx/{tx_hash}")
    print(f"Amount: {amount_eth:.2f} ETH")
    # You can integrate with Telegram, Slack, Discord here
