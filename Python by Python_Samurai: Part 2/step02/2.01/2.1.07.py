lst = [
    {
     'id': 1, 'name': 'fruits',
     'lst': ['apples', 'bananas', 'oranges']
    },
    {
     'id': 2, 'name': 'vegetables',
     'lst': ['potato', 'tomatoes', 'cucumbers']
    },
    {
     'id': 3, 'name': 'milk products',
     'lst': ['milk', 'ice cream', 'cheese']
    }
]       
# продолжите решение здесь
new_lst = [d['lst'] for d in lst]
print(new_lst)
