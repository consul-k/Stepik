gen = (key for key, value in computer_products.items() if 20000 >= value >= 15000)
for key in gen:
    print(key)
