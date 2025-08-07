products = [
    {"name": "Laptop", "category": "Electronics", "price": 1000},
    {"name": "Headphones", "category": "Electronics", "price": 200},
    {"name": "Coffee Maker", "category": "Home Appliances", "price": 150},
    {"name": "Blender", "category": "Home Appliances", "price": 120}
]

grouped_products = {}

for product in products:
    category = product["category"]
    item = {"name": product["name"], "price": product["price"]}
    if category not in grouped_products:
        grouped_products[category] = []
    grouped_products[category].append(item)

print(grouped_products)
