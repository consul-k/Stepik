def print_goods(goods):
    sorted_goods = sorted(goods, key=lambda x: (x['color'].lower(), -x['model']))

    for item in sorted_goods:
        print(f"Производитель: {item['make']}, модель: {item['model']}, цвет: {item['color']}")
