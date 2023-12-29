'''

    Часть кода уже написана.
    Выведите на экран __dict__ экземпляра my с помощью print.

Sample Input:


Sample Output:

{'name': 'Masha'}

'''

class MyClass:
    name = 'Vasya'

my = MyClass()
my.name = 'Masha'

# Напишите ваш код:
print(my.__dict__)
