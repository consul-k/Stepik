cont = ['планшеты', 'носки', 'куклы', 'смартфоны', 'ноутбуки', 'футболки', 'lego']
toys = ['куклы', 'lego', 'машинки']
cloth = ['джинсы', 'носки', 'футболки']

# продолжите решение здесь
stuff = set(toys + cloth)
result = set(cont) - stuff
print(' '.join(sorted(result)))
