'''

Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные часы в этот момент.

Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).

Учтите, что число n может быть больше, чем количество минут в сутках.

Sample Input 1:

137

Sample Output 1:

2 17

Sample Input 2:

2879

Sample Output 2:

23 59

Sample Input 3:

1511

Sample Output 3:

1 11

Sample Input 4:

608862

Sample Output 4:

19 42

'''

a = int(input())
print(a//60%24, a%60)
