# объявление функции
def draw_triangle():
    height = 8
    width = 15
    for i in range(height):
        stars = '*' * (2 * i + 1)
        spaces = ' ' * (height - i - 1)
        print(spaces + stars)
        
# основная программа
draw_triangle()  # вызов функции
