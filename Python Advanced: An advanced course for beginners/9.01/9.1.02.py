lst = set(input().split())
n = input()
print(f'Количество уникальных обитателей в Лесном Реестре: {len(lst)}')
if n in lst:
    print(f"Обитатель '{n}' зарегистрирован.")
else:
    print(f"Обитатель '{n}' не зарегистрирован.")
