# Создайте только вложенные функции:
def buy():
    def check_balance():
        if price > balance:
            return False
        else:
            return True

    def change_balance():
        global balance
        balance -= price

    if check_balance():
        change_balance()
        print("Покупка осуществлена")
    else:
        print("Недостаточно средств")

def show_balance():
    print(f"Ваш баланс: {balance}")

# Часть кода уже написана, используйте, но не меняйте:
balance = int(input())  # баланс покупателя
price = int(input())    # цена за товар
buy()                   # процесс покупки
show_balance()          # показывает баланс
