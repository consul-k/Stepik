'''

Дополните приведенный код, чтобы он вывел элементы множества fruits, каждый на отдельной строке, 
отсортированные по убыванию (в обратном лексикографическом порядке).

Примечание. Выводите каждый элемент множества на отдельной строке.

'''

fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}

sorted_f= sorted(fruits, reverse=True)
print(*sorted_f, sep='\n')
