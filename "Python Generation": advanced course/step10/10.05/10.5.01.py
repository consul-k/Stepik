'''

Дополните приведенный код, используя генератор, так чтобы получить словарь result , 
в котором ключом будет позиция числа в списке numbers (начиная с 0), а значением – его квадрат.

Примечание. Выводить содержимое словаря result не нужно.

'''

numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]

result = {i: numbers[i]**2 for i in range(len(numbers))}
