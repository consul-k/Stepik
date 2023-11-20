'''

Давайте считать человека подростком, если его возраст находится в пределах от 12 до 17 лет включительно. 
Напишите функцию is_person_teenager , которая помогает по возрасту определить является ли человек подростком или нет.

Функция is_person_teenager принимает на вход возраст человека и возвращает True или False

Нужно написать только определение функций is_person_teenager 

Sample Input 1:

8

Sample Output 1:

False

Sample Input 2:

15

Sample Output 2:

True

'''

def is_person_teenager(n):
    if n <= 17 and n >=12:
        return True
    return False
