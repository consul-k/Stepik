a = list(map(int, input().split()))
for i in a:
    if i <= 0:
        print(False)
        break
else:
    print(True)
