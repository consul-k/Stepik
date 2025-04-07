def print_goods(goods):
    parsed_goods = []
    for item in goods:
        name, price = item.split(":")
        parsed_goods.append((name.strip(), float(price.strip())))

    sorted_goods = sorted(parsed_goods, key=lambda x: (-x[1], x[0].lower()))

    for name, price in sorted_goods:
        print(f"{price:.2f} - {name}")
