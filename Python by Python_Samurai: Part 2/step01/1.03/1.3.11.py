def check_cities(cities):
    cities = cities.lower().split()
    for i in range(len(cities)-1):
        last_letter = cities[i][-1]
        if last_letter in 'ыьъ':
            last_letter = cities[i][-2]
        if cities[i+1][0] != last_letter:
            return "НЕТ"
    return "ДА"

cities_str = input()
print(check_cities(cities_str))
