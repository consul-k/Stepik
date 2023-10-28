'''

Вам дано целое число n. Нужно определить, что число является палиндромом (слева направо и справа налево читается одинаково). 
Примеры палиндромов: 121, 1331, 222, 2, 11, 56165.

В случае, если число является палиндромом, выведите True, в ином случае - False.

Для тех, кто уже прошел уроки по строкам: сможете решить эту задачу в целых числах без приведения к строке?

Sample Input 1:

1331

Sample Output 1:

True

Sample Input 2:

-1331

Sample Output 2:

False

Sample Input 3:

30

Sample Output 3:

False

Sample Input 4:

11

Sample Output 4:

True

Sample Input 5:

123123

Sample Output 5:

False

Sample Input 6:

33

Sample Output 6:

True

Sample Input 7:

0

Sample Output 7:

True

Sample Input 8:

5445

Sample Output 8:

True

Sample Input 9:

-5445

Sample Output 9:

False

'''

n = input()
print(n == n[::-1])
