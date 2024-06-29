def main():
    n = int(input()) 
    transactions = {}

    for _ in range(n):
        operation, last_name, amount = input().split()
        amount = int(amount)

        if last_name not in transactions:
            transactions[last_name] = 0

        if operation == 'приход':
            transactions[last_name] += amount
        elif operation == 'расход':
            transactions[last_name] -= amount

    # Фильтруем нулевые остатки и сортируем по фамилии
    result = {k: v for k, v in sorted(transactions.items()) if v != 0}

    for last_name, balance in result.items():
        print(last_name, balance)

if __name__ == "__main__":
    main()
