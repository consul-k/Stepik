# исходные данные        
lst = [
    {'num_1': 6, 'num_2': 3, 'num_3': 9},
    {'num_1': 3, 'num_2': 9},
    {'num_1': 2, 'num_2': 11, 'num_3': 15},
    {'num_1': 0, 'num_2': 7},
    {'num_1': 1, 'num_2': 5, 'num_3': 7}
    ]        

# продолжите решение здесь
for i in lst:
    match i:
        case {'num_1': num_1, 'num_3': num_3}:
            print(num_1 + num_3)
        case {'num_1': num_1, 'num_2': num_2}:
            print(num_1 + num_2)
