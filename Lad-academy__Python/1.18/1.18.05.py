n = int(input())
total = set()

for word in range(n):
    word = set(input().lower())
    total.update(word)
    
print(len(total))
