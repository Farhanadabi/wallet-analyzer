class Analyzer:
    def __init__(self, wallet_data, token_data, transaction_data):
        self.wallet_data = wallet_data
        self.token_data = token_data
        self.transaction_data = transaction_data

    def analyze_buying_patterns(self, token_symbol):
        buying_transactions = []
        for transaction in self.transaction_data:
            if transaction['type'] == 'buy' and token_symbol in transaction['token']:
                buying_transactions.append(transaction)
        return buying_transactions

    def analyze_selling_patterns(self, token_symbol):
        selling_transactions = []
        for transaction in self.transaction_data:
            if transaction['type'] == 'sell' and token_symbol in transaction['token']:
                selling_transactions.append(transaction)
        return selling_transactions

    def summarize_analysis(self, token_symbol):
        buying_patterns = self.analyze_buying_patterns(token_symbol)
        selling_patterns = self.analyze_selling_patterns(token_symbol)
        return {
            'buying_patterns': buying_patterns,
            'selling_patterns': selling_patterns
        }