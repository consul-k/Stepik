def calculate_final_price(base_price, discount=0, shipping_fee=0):
    if isinstance(discount, str):
        discount = discount.strip()
        discount = float(discount) if discount else 0
    else:
        discount = float(discount)

    if isinstance(shipping_fee, str):
        shipping_fee = shipping_fee.strip()
        shipping_fee = float(shipping_fee) if shipping_fee else 0
    else:
        shipping_fee = float(shipping_fee)

    final_price = base_price - (base_price * discount / 100) + shipping_fee
    print(f"Итоговая сумма заказа: {final_price}")
