text = input()

cnt = text.lower().count('магия')
print(f'Магия найдена {cnt} раз(а).')

if cnt % 2 == 0 or cnt == 0:
    print(f"Результат: {text.replace(' ', '')[::-1]}")
else:
    print(f"Результат: {''.join([i for i in text if text.count(i) == 1])}")
