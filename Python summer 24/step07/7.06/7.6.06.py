def draw_triangle(fill, base):
    for i in range(base // 2):
        print(fill * (i + 1))
    for i in range(base // 2, -1, -1):
        print(fill * (i + 1))
        
fill = input()
base = int(input())
draw_triangle(fill, base)
