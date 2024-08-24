n = int(input())
cities = set()
repeat = False

for _ in range(n+1):
    city = input()
    if city in cities:
        repeat = True
    cities.add(city)
    
if repeat:
    print('REPEAT')
else:
    print('OK')
