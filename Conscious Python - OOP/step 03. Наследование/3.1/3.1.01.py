'''

    Создайте класс Gomer.
    Создайте в классе Gomer метод __init__(self, name), который создает атрибут name.
    Создайте пустой класс Daughter и сделайте его дочерним классом для Gomer. Используйте pass для пустого класса.
    Создайте экземпляр daughter1 для класса Daughter и присвойте атрибуту name значение Lisa.
    Выведите на экран значение атрибута name через экземпляр daughter1.

Sample Input:


Sample Output:

Lisa

'''

class Gomer:
    def __init__(self, name):
        self.name = name
        
class Daughter(Gomer):
    pass

daughter1 = Daughter('Lisa')
print(daughter1.name)
