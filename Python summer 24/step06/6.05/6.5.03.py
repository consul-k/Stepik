text = input().lower().split()
res = 0

for i in text:
    if i == 'a' or i == 'an' or i == 'the':
        res += 1
print(f'Общее количество артиклей: {res}')
