'''

Ваша задача создать список из n строк. Программа сперва будет принимать натуральное число n, а затем n строк в каждой отдельной строке. 
В качестве ответа выведите получившийся список.

Sample Input 1:

4
Джон
Пол
Ринго
Джордж

Sample Output 1:

['Джон', 'Пол', 'Ринго', 'Джордж']

Sample Input 2:

2
black
white

Sample Output 2:

['black', 'white']

'''

s = []
for _ in range(int(input())):
    s.append(input())
print(s)
