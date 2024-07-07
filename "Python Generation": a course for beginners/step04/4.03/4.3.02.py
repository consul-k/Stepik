a = int(input())
b = int(input())
c = int(input())
if a == b and b == c and c == a:
    print('Равносторонний')
elif a != b and b != c and c != a:
    print('Разносторонний')
elif (a == b and b != c and a != c) or (b == c and a != c and a != b) or (a == c and b != c and b != a):
    print('Равнобедренный')
