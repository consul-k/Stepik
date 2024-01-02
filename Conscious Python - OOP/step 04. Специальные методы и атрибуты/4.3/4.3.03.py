'''

Часть кода уже написана, вам нужно лишь объявить методы __ge__, __le__. Эти методы, сравнивают экземпляры по количеству страниц в книге на ">=" и "<=".

 
# напоминашка
__le__ # меньше или равно
__ge__ # больше или равно

Sample Input:

Sample Output:

True
True
True

'''

class Books:
    def __init__(self, book_name, book_page):
        self.book_name = book_name
        self.book_page = book_page

    # ваш код для __le__ и __ge__
    def __ge__(self, other):
        return self.book_page >= other.book_page

# код ниже не меняйте, ради вселенной 
book1 = Books('Война и мир', 1360)
book2 = Books('Собака Баскервилей', 112)
book3 = Books('Скотный двор', 112)

print(book1 >= book2)
print(book1 >= book3)
print(book2 <= book3)
