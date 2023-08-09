'''

Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. 
Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.

'''

s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

result = dict(zip([i for i in s.split()], [s.count(i) for i in s.split()]))
m = max(result.values())
list_m = []

for word in result:
    if result[word] == m:
        list_m.append(word)
        
list_m = sorted(list_m)

print(list_m[0])
