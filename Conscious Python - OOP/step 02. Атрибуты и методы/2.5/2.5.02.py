'''

    Создайте класс Time
    Создайте статический метод с помощью декоратора @staticmethod, и назовите его count_time. В аргументах укажите (distance, speed).
    Внутри метода лишь одна операция, подсчёт времени по формуле (time = distance / speed). Метод возвращает результат с помощью return
    Вызовете метод count_time через класс, и укажите в аргументах (500, 100). Вызывать нужно через print(Класс.метод()), так как метод использует return.

Sample Input:

Sample Output:

5.0

'''

class Time:
    @staticmethod
    def count_time(distance, speed):
        time = distance / speed
        return time
    
print(Time.count_time(500, 100))
