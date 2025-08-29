res = 0

for i in range(int(input())):
    i = int(input())
    if i % 13 != 0:
        res += i
print(res)
