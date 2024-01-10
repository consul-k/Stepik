'''

Вводные данные:

Расстояние от города до деревни: 1000 м. Три человека идут отдельно друг от друга и уже прошли определённое расстояние (distance) от города до деревни. 
Сделайте так, чтобы каждый из них мог знать, сколько метров им ещё нужно пройти.
Задание:

    Часть кода уже готова, заполните оставшуюся часть по заданию.
    Создайте метод add_distance с аргументами (self, dist). Метод принимает число (dist), и вычисляет, сколько ещё нужно пройти человеку, 
    чтобы завершить путь и выводит оставшийся путь на экран.
    Вызовите метод, для всех трёх экземпляров (vasya, masha, slava, по очереди). В аргументах укажите 1000. 

Sample Input:

Sample Output:

800
600
300

'''

class Village:
    distance = 0
    # ваш метод add_distance
    def add_distance(self, a = 1000):
        print(a-self.distance)

vasya = Village()
masha = Village()
slava = Village()

vasya.distance = 200
masha.distance = 400
slava.distance = 700

# вызовите методы для каждого экземпляра:
vasya.add_distance()
masha.add_distance()
slava.add_distance()
