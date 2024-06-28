n = int(input())
cities={}
for _ in range(n):
    city, population = input().split('=')
    cities[city] = int(population)

millionaire_cities = [city for city, pop in cities.items() if pop >= 1000000]

if millionaire_cities:
    print(*sorted(millionaire_cities), sep='\n')
else:
    print("NO SUCH CITIES")
