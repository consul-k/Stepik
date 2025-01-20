# Создайте только вложенные функции:
def buy():
    def check_balance():
        # Проверяем, достаточно ли средств на балансе
        if price > balance:
            return False
        else:
            return True

    # Проверка результата функции check_balance()
    if check_balance():
        print("Покупка осуществлена")
    else:
        print("Недостаточно средств")

# Часть кода уже написана, используйте, но не меняйте:
balance = int(input())  # баланс покупателя
price = int(input())    # цена за товар
buy()                   # процесс покупки
