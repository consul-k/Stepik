'''

Ученики 10 класса онлайн-школы BEEGEEK получили задание прочесть на летних каникулах три книги:

    "Что такое математика?";
    "Математическая составляющая";
    "100 гениальных идей по математике".

Оказалось, что n учеников прочитали первую книгу, m учеников — вторую, k учеников — третью. 
Также известно, что x учеников прочли первую или вторую, или обе эти книги, y учеников — вторую или третью, или обе, 
z учеников — первую и третью, или хотя бы одну из этих двух книг. 
Полностью выполнили задание только t учеников. Всего в 10 классе учится aa учеников. 
Напишите программу, которая выводит сколько учеников:

    прочитали только одну книгу;
    прочитали две книги;
    не прочитали ни одной из рекомендованных книг.

Формат входных данных
На вход программе подаются числа n,m,k,x,y,z,t,a, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести три числа в соответствии с условием задачи, каждое на отдельной строке.
Тестовые данные 🟢

Sample Input:

19
18
22
32
33
35
2
50

Sample Output:

29
12
7

'''

n = int(input())
m = int(input())
k = int(input())
x = int(input())
y = int(input())
z = int(input())
t = int(input())
a = int(input())

s1 = n + m - t - x
s2 = n + k - t - z
s3 = m + k - t - y

book_n = n - t - s1 - s2
book_m = m - t - s1 - s3
book_k = k - t - s2 - s3

single = book_n + book_m + book_k
double = s1 + s2 + s3
zero = a - (book_n + book_m + book_k + s1 + s2 + s3 + t)

print(single)
print(double)
print(zero)
