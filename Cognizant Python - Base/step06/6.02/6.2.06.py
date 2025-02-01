def balance_decorator(func):
    def wrapper(num):        
        if num > 0:
            func(num)
            print('Баланс пополнен!')
        elif num < 0 and balance >= abs(num):
            func(num)
            print('Покупка совершена!')
        else:
            print('Недостаточно средств!')
    return wrapper

@balance_decorator
def change_balance(num):
    """Функция изменяет баланс"""
    global balance
    balance += num

balance = int(input())
change_balance(int(input()))
change_balance(int(input()))
change_balance(int(input()))
