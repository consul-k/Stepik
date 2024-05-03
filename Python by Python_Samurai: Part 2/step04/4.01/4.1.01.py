# вводные данные        
lst = [1, 5.6, '3', [1, 2], (4, 7), {'a': 4}, True]        

# продолжите решение здесь
for i in lst:
    match i:
        case bool():
            print(f'Это тип данных - <class \'bool\'>')
        case dict():
            print(f'Это тип данных - <class \'dict\'>')
        case tuple():
            print(f'Это тип данных - <class \'tuple\'>')
        case list():
            print(f'Это тип данных - <class \'list\'>')
        case float():
            print(f'Это тип данных - <class \'float\'>')
        case int():
            print(f'Это тип данных - <class \'int\'>')
