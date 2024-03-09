'''

Вы вводите любое целое число, например: 91. Это число не палиндром, поэтому переворачиваем его и складываем:
91 + 19. Получится 110. Данное число также не является палиндромом, поэтому повторяем операцию до тех пор, пока не встретим палиндром:
110 + 011. Получится число 121. Оно является палиндромом.

Sample Input:

87

Sample Output:

165
726
1353
4884

'''

def soln(num):
    results = []
    while True:
        rev_num = int(str(num)[::-1])
        num = num + rev_num
        results.append(num)
        if str(num) == str(num)[::-1]:
            break
    return results

n = int(input())
result = soln(n)
for x in result:
    print(x)
