filter_persons = filter(lambda pers: pers['rating'] >= 4.5, persons)
sorted_persons = sorted(filter_persons, key=lambda pers: pers['name'])

for p in sorted_persons:
    print(p['name'])
