'''

Подвиг 2. Объявите функцию с именем is_triangle, которая принимает три стороны треугольника (целые числа) и проверяет, 
можно ли из переданных аргументов составить треугольник. (Напомню, что у любого треугольника длина третьей стороны всегда должна быть 
меньше суммы двух других). Если  проверка проходит, вернуть булево значение True, иначе - значение False.

Вызывать функцию не нужно, только задать.

Sample Input:

3 4 5

Sample Output:

True

'''

def is_triangle(a,b,c):
    if c < a + b:
        return True
    else:
        return False
