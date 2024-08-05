city1 = input()
city2 = input()
city3 = input()

cities = [city1, city2, city3]
shortest_city = min(cities, key=len)
longest_city = max(cities, key=len)

print(shortest_city)
print(longest_city)
