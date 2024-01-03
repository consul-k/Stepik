'''

Создайте класс, нужные методы, атрибуты и экземпляр. Затем, выведите на экран информацию об экземпляре для программистов. 
Пример вывода написан ниже (Sample Output). Используйте информацию из примера, чтобы написать код.

Имя класса, можете написать руками, или используйте команду в f-строке: f"self.__class__.__name__" .
Команда выводит имя класса.

Sample Input:

Sample Output:

Класс: Car, Атрибуты экземпляра: {'model': 'toyota corolla', 'color': 'black', 'year': 2023}

'''

class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
        
    def __repr__(self):
        return f"Класс: {self.__class__.__name__}, Атрибуты экземпляра: {self.__dict__}"
    
car = Car('toyota corolla', 'black', 2023)
print(car)
