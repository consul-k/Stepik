def create_actor(**kwargs):
    dic={
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 47,
    }
    for k,v in kwargs.items():
        dic[k] = v
    return dic
