'''

Исправьте код с предыдущего задания так, чтобы на экран вывело bye и hello
Код с предыдущего задания:

Sample Input:

Sample Output:

bye
hello

'''

def outer() -> None:
    def say_hello() -> None:
        print('hello')

    def say_bye() -> None:
        print('bye')
        
    say_bye()
    say_hello()

outer()
