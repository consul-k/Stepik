res = 0
for i in range(int(input())):
    i = input()
    if i == i[::-1]:
        res += 1
print(res)
