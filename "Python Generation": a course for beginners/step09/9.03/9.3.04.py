word = input()
res = 0
for l in word:
    if l.islower() and l.isalpha():
        res += 1
print(res)
