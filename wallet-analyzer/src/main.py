import requests
from solscan_api import get_wallet_overview, get_token_balances, get_transaction_history
from analyzer import Analyzer

def main():
    wallet = input("Enter the wallet address to analyze: ")
    
    print("Fetching wallet overview...")
    overview = get_wallet_overview(wallet)
    print(overview)

    print("Fetching token balances...")
    token_balances = get_token_balances(wallet)
    print(token_balances)

    print("Fetching transaction history...")
    transactions = get_transaction_history(wallet)
    print(transactions)

    analyzer = Analyzer(token_balances, transactions)
    buying_selling_patterns = analyzer.analyze()
    print("Buying and Selling Patterns:")
    print(buying_selling_patterns)

if __name__ == "__main__":
    main()