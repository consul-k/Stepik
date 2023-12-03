'''

Перед вами два списка одинаковой длины keys и values

Ваша задача создать словарь result, в котором пара ключ-значение берется из значений списков, стоящих на одинаковых индексах. 
В качестве ответа выведите словарь result

Sample Input:

Sample Output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50, 'Sixty': 60, 'Seventy': 70, 'Eighty': 80, 'Ninety': 90, 'One hundred': 100}

'''

keys = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'One hundred']
values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

result = dict(zip(keys, values))
print(result)
