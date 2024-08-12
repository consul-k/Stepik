text = input()
a = {i for i in text}
if len(text) == len(a):
    print('YES')
else:
    print('NO')
