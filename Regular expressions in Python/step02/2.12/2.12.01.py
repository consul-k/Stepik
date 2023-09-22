'''

Напишите регулярное выражение, которое найдёт в тексте следующие языки программирования: JavaScript, C++, Python.
Что нужно найти:

Последовательности: JavaScript, C++, Python

Sample Input 1:

Когда я перешёл с C++ на Python - я почувствовал себя богом.

Sample Output 1:

C++ Python

Sample Input 2:

Через час те из вас, кто выучит C++, будут завидовать мёртвым.

Sample Output 2:

C++

Sample Input 3:

JavaScript is a high-level, often just-in-time compiled language.

Sample Output 3:

JavaScript

Sample Input 4:

Python C++ JavaScript

Sample Output 4:

Python C++ JavaScript

'''

regex = r'((?:JavaScript)|(?:C\+\+)|(?:Python))'
