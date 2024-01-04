'''

Подвиг 4. Вводится строка со словами, разделенными пробелом. 
Необходимо первый пробел заменить на одинарную кавычку, а все остальные - на двойные. Результирующую строку отобразить на экране.

Sample Input:

My best friend is Python!

Sample Output:

My'best"friend"is"Python!

'''

s = input().replace(' ','\'',1).replace(' ','\"')
print(s)
