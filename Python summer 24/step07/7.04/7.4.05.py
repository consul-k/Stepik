def get_shipping_cost(quantity):
    if quantity == 1:
        return 1000
    else:
        return 1000 + (quantity-1)*120

n = int(input())

print(get_shipping_cost(n))
