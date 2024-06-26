a = input()
check = 'aeiouyAEIOUY'
res = ''
for i in a:
    if i in check:
        res += i.upper()
    else:
        res += i.lower()
print(res)
