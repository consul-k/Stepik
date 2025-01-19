def change_balance(money):    
    global balance
    try:
        money = int(money)
        balance += money
        print(balance)
    except ValueError:
        print('Введите число')


balance = 1000
change_balance(input())
