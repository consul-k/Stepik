s = input()
if s[0].isupper() and s[-1].isupper() and s[1:-1].islower():
    print(True)
else:
    print(False)
