'''

При помощи генератора-списка создайте список [1, 2, 3, ..., n], само натуральное число n будет поступать на вход вашей программе.

В качестве ответа просто выведите получившийся список

Sample Input 1:

1

Sample Output 1:

[1]

Sample Input 2:

5

Sample Output 2:

[1, 2, 3, 4, 5]

Sample Input 3:

9

Sample Output 3:

[1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

s = [i for i in range(1,int(input())+1)]
print(s)
