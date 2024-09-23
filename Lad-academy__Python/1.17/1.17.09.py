d = {}
for _ in range(int(input())):
    key, value = input().split(': ')
    d[key.lower()] = value

m = int(input())
ask = []
for _ in range(m):
    ask.append(input().lower())
    
for word in ask:
    print(d.get(word, 'Не найдено'))
