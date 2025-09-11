year = int(input())
prep = int(input())
n = input()
name = input().replace(' ', '')

ind = (sum(int(i) for i in n)) + len(name)
print(f'Год прорыва: {year + (prep * ind)}')
