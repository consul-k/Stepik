res = dict()

for _ in range(5):
    key = input()
    value = int(input())
    res[key] = value 
    
for key, value in res.items():
    print(f'{key} - {value} гр. сахара!')
