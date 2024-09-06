keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']

dictionary = dict()
for key, value in zip(keys, values):
    dictionary[key] = value
print(dictionary)
