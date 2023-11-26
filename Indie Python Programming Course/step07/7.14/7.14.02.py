'''

Напишите декоратор repeater, который дважды вызывает декорированную функцию

@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 7) # после этого распечатается две строки со значением 14
multiply(5, 3) # после этого распечатается две строки со значением 15

Ваша задача написать только определение функции декоратора repeater

'''

def repeater(func):
    def inner(*args, **kwargs):
        for _ in range(2):
            func(*args, **kwargs)
    return inner
