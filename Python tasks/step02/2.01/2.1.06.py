a = input().split()
for word in a:
    if word[0] != word[0].upper():
        print(False)
        break
else:
    print(True)
