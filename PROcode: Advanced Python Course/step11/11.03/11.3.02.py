def get_wallet_balance(transactions):
    if not transactions:
        return 0
    return transactions[0] + get_wallet_balance(transactions[1:])
