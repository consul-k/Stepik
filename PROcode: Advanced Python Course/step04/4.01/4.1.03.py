s = list(map(int, input().split()))
for i in s:
    if i % 7 == 0:
        print(i)
        break
else:
    print(None)
