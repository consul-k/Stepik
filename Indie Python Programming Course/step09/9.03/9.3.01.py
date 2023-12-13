'''

Ваша задача выполнить сериализацию словаря из данного задания и сохранить полученную json-строку в переменную json_data

В качестве ответа ваша программа должна вывести на экран значение переменной json_data

'''

from string import ascii_lowercase
import json

alphabet = {}
cnt = 1
for i in ascii_lowercase:
    alphabet[i] = cnt
    cnt += 1

json_data = json.dumps(alphabet)
print(json_data)
