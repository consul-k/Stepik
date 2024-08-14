# объявление функции
def draw_triangle(fill, base):
    height = (base // 2) + 1

    for i in range(1, height + 1):
        print(fill * i)

    for i in range(height - 1, 0, -1):
        print(fill * i)

fill = input()
base = int(input())

draw_triangle(fill, base)
