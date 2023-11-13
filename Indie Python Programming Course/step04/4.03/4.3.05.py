'''

Программа принимает на вход одно натуральное число. Ваша задачи найти сколько раз встречается цифра 7 в этом числе

Sample Input 1:

777

Sample Output 1:

3

Sample Input 2:

127

Sample Output 2:

1

'''

n = int(input())
s = []
while n > 0:
    s.append(n%10)
    n//=10
print(s.count(7))
