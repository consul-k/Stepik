text = input().split()
res = 0
res += text.count('a')
res += text.count('an')
res += text.count('the')
res += text.count('A')
res += text.count('An')
res += text.count('The')
print(f'Общее количество артиклей: {res}')
