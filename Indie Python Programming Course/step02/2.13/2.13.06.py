'''

В вашем распоряжении список numbers. Ваша задача отсортировать список numbers в порядке убывания  и вывести на экран результат.

Sample Input:

Sample Output:

[472, 448, 422, 284, 198, 181, 32, 29, -20, -139, -214, -895, -917, -964, -986, -989]

'''

numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
numbers.sort(reverse=True)
print(numbers)
