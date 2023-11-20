'''

Напишите функцию print_initials(name, surname, middlename), которая принимает три параметра:

    name – имя человека;
    surname – фамилия человека;
    middlename– отчество человека;

а затем выводит на печать фамилию и инициалы в определенном формате (первая буква фамилии должна стать заглавной, 
все остальные строчные; в имени и отчестве остаются только по одной букве в верхнем регистре).

Ваша задача дописать только тело функции print_initials

Sample Input 1:

Мария
Иванова
Филлиповна

Sample Output 1:

Иванова М.Ф.

Sample Input 2:

евгЕний
петросян
ВаГАнович

Sample Output 2:

Петросян Е.В.

'''

def print_initials(name, surname, middlename):
    print(f'{surname.capitalize()} {name.capitalize()[0]}.{middlename.capitalize()[0]}.')

name = input()
surname = input()
middlename = input()

print_initials(name, surname, middlename)
