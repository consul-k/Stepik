'''

    Часть кода уже написана.
    Переменная input_word принимает разные строки.
    Создайте метод __str__ , чтобы команда print(person) выводила сообщение "Да здравствует input_word!". 
    Естественно input_word здесь переменная, и будет принимать разные слова. Пример результатов ниже. 

Sample Input 1:

Вася

Sample Output 1:

Да здравствует Вася!

Sample Input 2:

Вселенная

Sample Output 2:

Да здравствует Вселенная!

Sample Input 3:

Будда

Sample Output 3:

Да здравствует Будда!

'''

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Да здравствует {self.name}!'

# Код ниже пожалуйста не меняйте:        
input_word = input()
person = Person(input_word)
print(person)
