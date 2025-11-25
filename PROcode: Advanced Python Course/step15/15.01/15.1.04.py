cities_input = input()

cities_tuple = tuple(city.strip() for city in cities_input.split(','))

print(cities_tuple)

print(f"Последний город тура: {cities_tuple[-1]}")
