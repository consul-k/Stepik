def persons_sort(d: dict):
    return d['bad habits'], -d['age']


print(*sorted(persons, key=persons_sort), sep='\n')
