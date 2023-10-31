'''

Вашей программе на вход подается массив содержащий объекты со структурой ниже.

{
    "id": 1,
    "parents": [1,2,3,4],
    "chief": {
        "name": "Paul",
        "age": 50
    },
    "age": 22
}

Определите максимальное значение во всех полях age этого объекта.

Ввод:

d – json-объект

Вывод:

res – максимальный возраст

Sample Input 1:

[{"id": 1,"parents": [1,2,3,4],"chief": {"name": "Paul","age": 50},"age": 22}, {"id": 1,"parents": [1,2,3,4],"chief": {"name": "Paul","age": 62},"age": 80}]

Sample Output 1:

80

Sample Input 2:

[{"id": 1,"parents": [1,2,3,4],"chief": {"name": "Paul","age": 100},"age": 22}, {"id": 1,"parents": [1,2,3,4],"chief": {"name": "Paul","age": 62},"age": 80}]

Sample Output 2:

100

Sample Input 3:

[{"id": 1,"parents": [1,2,3,4],"chief": {"name": "Paul","age": 50},"age": 100}, {"id": 1,"parents": [1,2,3,4],"chief": {"name": "Paul","age": 62},"age": 80}]

Sample Output 3:

100

Sample Input 4:

[{"id": 1,"parents": [1,2,3,4],"chief": {"name": "Paul","age": 50},"age": 22}, {"id": 1,"parents": [1,2,3,4],"chief": {"name": "Paul","age": 100},"age": 80}]

Sample Output 4:

100

Sample Input 5:

[{"id": 1,"parents": [1,2,3,4],"chief": {"name": "Paul","age": 50},"age": 22}]

Sample Output 5:

50

'''

import json
d = json.loads(input())

#ваш код (используйте переменную d)
l = []
for i in range(len(d)):
    l.append(d[i]['age'])
    l.append(d[i]['chief']['age'])

print(max(l))
