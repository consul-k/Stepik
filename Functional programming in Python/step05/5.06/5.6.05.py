def calculate(x,y,operation='a'):
    def addition(x,y):
        return x+y
    def subtraction(x,y):
        return x-y
    def division(x,y):
        if y == 0:
            return 'На ноль делить нельзя!'
        else:
            return x/y
    def multiplication(x,y):
        return x*y
    if operation == 'a':
        print(addition(x,y))
    elif operation == 's':
        print(subtraction(x,y))
    elif operation == 'd':
        print(division(x,y))
    elif operation == 'm':
        print(multiplication(x,y))
    else:
        print('Ошибка. Данной операции не существует')
