n = int(input())
if n%5==0 and n%3==0:
    print('КрастиКрабс')
elif n%3 == 0:
    print('Красти')
elif n%5 == 0:
    print('Крабс')
else:
    print(n)
