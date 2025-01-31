def input_kassa(cash):
    def operation_with_kassa(number):
        nonlocal cash
        cash = cash + number
    def print_kassa():
        print(cash)
    return operation_with_kassa, print_kassa

a, b = input_kassa(0)
[a(int(input())) for _ in "1234"]
b()
