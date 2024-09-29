import json

with open('account.json', 'r') as f:
    config = json.load(f)

TELEGRAM_ACCOUNTS = config.get('TELEGRAM_ACCOUNTS', [])