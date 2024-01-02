'''

    Большая часть кода уже написана. Создайте метод(ы), чтобы результаты сравнения были как в коде.
    Метод(ы) сравнивают длину (len) списков.

Напоминашка:
__lt__ # меньше
__gt__ # больше

Sample Input:

Sample Output:

True
False

'''

class Lists:
    def __init__(self, lists):
        self.lists = lists

    # ваш метод(ы)
    def __lt__(self, other):
        return len(self.lists) < len(other.lists)
    
# код ниже не меняйте, во имя вселенной
lst1 = Lists(["a", "b", "c"])
lst2 = Lists([1, 2, 3, 4, 5])
print(lst1 < lst2)  # True
print(lst1 > lst2)  # False
