s = input()
index = s.find('tail')  # Находим первое вхождение "tail"
result = s[index + len('tail'):]  # Отрезаем хвост
print(result)
