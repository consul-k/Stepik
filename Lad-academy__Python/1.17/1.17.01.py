syn = {}

for _ in range(int(input())):
    key, value = input().split()
    syn[key] = value
    syn[value] = key
               
ask = input()
print(syn.get(ask))
