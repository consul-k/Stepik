secret = input()
rev = {}

for i in range(int(input())):
    key, value = input().split()
    rev[key.strip(':')] = int(value)
    
for i in secret:
    for k in rev:
        if secret.count(i) == rev[k]:
            secret = secret.replace(i,k)
            
print(secret)
