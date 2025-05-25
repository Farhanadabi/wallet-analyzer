# Wallet Analyzer

## Overview
The Wallet Analyzer is a Python project designed to analyze specific cryptocurrency wallets for buying and selling patterns of tokens. It interacts with the Solscan API to fetch wallet overviews, token balances, and transaction histories, providing insights into wallet activities.

## Project Structure
```
wallet-analyzer/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── analyzer.py
│   ├── solscan_api.py
│   └── utils.py
├── requirements.txt
└── README.md
```

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd wallet-analyzer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To analyze a wallet, run the main application:
```
python src/main.py
```

You will be prompted to enter the wallet address you wish to analyze. The application will then fetch the relevant data and provide insights into buying and selling patterns.

## Features
- Fetch wallet overviews, token balances, and transaction histories using the Solscan API.
- Analyze transactions to identify buying and selling patterns of specific tokens.
- Utility functions for data processing and formatting.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.