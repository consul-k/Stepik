a = input()
for s in a:
    if not s.isdigit():
        print(False)
        break
else:
    print(True)
