res = 0
for i in range(int(input())):
    i = int(input())
    if i%3 == 0 and i%10 == 2:
        res += 1
print(res)
