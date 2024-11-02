def apply_discount(price, *discounts):
    for discount in discounts:
        price -= price * (discount / 100)
    return price
