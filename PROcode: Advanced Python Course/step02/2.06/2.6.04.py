def main():
    orders = {} 

    num_clients = int(input())

    for _ in range(num_clients):
        name = input()
        num_substances = int(input())

        substances = {}
        for _ in range(num_substances):
            line = input()
            substance, quantity = line.split()
            substances[substance] = int(quantity)

        orders[name] = substances

    print("Заказы клиентов:")
    for client, substances in orders.items():
        print(f"{client}:")
        for substance, quantity in substances.items():
            print(f"    {substance}: {quantity}")

if __name__ == "__main__":
    main()
