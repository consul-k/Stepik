name = input().replace(' ','')
number = sum(int(i) for i in input())
print(f'Код замка: {number}-{len(name)}')
