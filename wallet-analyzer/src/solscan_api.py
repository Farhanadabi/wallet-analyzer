import requests

BASE_URL = "https://public-api.solscan.io"
HEADERS = {
    "accept": "application/json",
    "User-Agent": "Mozilla/5.0"
}

def get_wallet_overview(wallet):
    url = f"{BASE_URL}/account/{wallet}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return {}
    try:
        return response.json()
    except Exception as e:
        print(f"JSON decode error: {e}")
        return {}

def get_token_balances(wallet):
    url = f"{BASE_URL}/account/tokens?account={wallet}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return []
    try:
        return response.json()
    except Exception as e:
        print(f"JSON decode error: {e}")
        return []

def get_transaction_history(wallet, limit=10):
    url = f"{BASE_URL}/account/transactions?address={wallet}&limit={limit}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return []
    try:
        return response.json()
    except Exception as e:
        print(f"JSON decode error: {e}")
        return []