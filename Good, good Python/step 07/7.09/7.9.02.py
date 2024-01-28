'''

Подвиг 4. Имеется программа (см. листинг ниже). Необходимо в теле функции func2 дописать команду,
которая бы меняла значение уже существующей переменной msg, объявленной в функции func1.

Sample Input:

Сергей
Балакирев

Sample Output:

Балакирев
Балакирев

'''

def func1():
    msg = input()

    def func2():
        nonlocal msg
        msg = input()
        print(msg)


    func2()        
    print(msg)


func1()
