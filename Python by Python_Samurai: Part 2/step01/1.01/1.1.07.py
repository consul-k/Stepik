s = input()
while '--' in s:
    s = s.replace('--', '-')
print(s)
