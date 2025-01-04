for product, quantity in stock.items():
    if quantity > 0:
        print(f"Товар: {product}, остаток {quantity} шт")
    else:
        print(f"Товар: {product}, к сожалению закончился")
