def format_token_balance(balance):
    return f"{balance['amount']} {balance['tokenSymbol']}"

def filter_transactions(transactions, token_symbol):
    return [tx for tx in transactions if tx.get('tokenSymbol') == token_symbol]

def calculate_profit_loss(buy_transactions, sell_transactions):
    total_buy = sum(tx['amount'] for tx in buy_transactions)
    total_sell = sum(tx['amount'] for tx in sell_transactions)
    return total_sell - total_buy

def parse_transaction_date(transaction):
    return transaction['date']  # Assuming 'date' is a key in the transaction dict

def summarize_wallet_activity(wallet_overview):
    return {
        'total_tokens': len(wallet_overview.get('tokens', [])),
        'total_transactions': wallet_overview.get('transactionCount', 0)
    }