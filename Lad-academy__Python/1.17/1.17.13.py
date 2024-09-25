d = {}
for _ in range(int(input())):
    l = input().split()
    d[l[0]] = [s for s in l[1:]]
    
for city in range(int(input())):
    city = input()
    for country in d:
        if city in d[country]:
            print(country)
