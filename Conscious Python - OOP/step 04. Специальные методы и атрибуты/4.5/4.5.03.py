'''

Задание:

    Часть кода уже написана.
    Сделайте так, чтобы экземпляры, с одинаковыми атрибутами и значениями, имели одинаковый хэш.

Sample Input:

Sample Output:

True

'''

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    # ваш код:
    def __hash__(self):
        return hash((self.model, self.color))


# код ниже не меняйте, ради вселенной
car1 = Car("toyota corolla", "black")
car2 = Car("toyota corolla", "black")
print(hash(car1) == hash(car2))
