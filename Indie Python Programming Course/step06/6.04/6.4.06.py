'''

Перед вами имеется словарь sweet

Удалите из него ключи ppu и type

Затем выведите словарь sweet в качестве ответа

'''

sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125,
}
del sweet['ppu']
del sweet['type']
print(sweet)
