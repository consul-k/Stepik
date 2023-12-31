'''

Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.

Формат входных данных
На вход программе в первой строке подается число nn – общее количество слов. Далее идут nn строк со словами.

Формат выходных данных
Программа должна вывести одно число – общее количество уникальных символов во всех словах без учета регистра.
Тестовые данные 🟢

Sample Input 1:

5
aAa
bB
ccc
dDdd
ppppP

Sample Output 1:

5

Sample Input 2:

4
авТорИтет
небо
машинА
Мёд

Sample Output 2:

13

Sample Input 3:

4
троС
рОст
сорт
тОрС

Sample Output 3:

4

'''

n = int(input())
total = set()

for word in range(n):
    word = set(input().lower())
    total.update(word)
    
print(len(total))
