burger_1 = ['булочка', 'мясо', 'сыр', 'помидор', '"1000 островов"', 'красный лук']
burger_2 = ['булочка', 'мясо', 'сыр', 'помидор', '"барбекю"', 'лук', 'огурец']

basic_ingredients = set(burger_1) & set(burger_2)
extra_ingredients = (set(burger_1) | set(burger_2)) - basic_ingredients

money = int(input())
basic_price = round(money * 2/3, 1)
extra_price = round(money * 1/3, 1)

result = {
    'Базовые ингредиенты': {
        'Продукты': sorted(list(basic_ingredients)),
        'Цена': basic_price
    },
    'Дополнительные ингредиенты': {
        'Продукты': sorted(list(extra_ingredients)),
        'Цена': extra_price
    }
}

print(f"Базовые ингредиенты: {result['Базовые ингредиенты']}")
print(f"Дополнительные ингредиенты: {result['Дополнительные ингредиенты']}")
