'''

Перед вами имеется словарь sweet

В отдельных строках распечатайте сперва значение ключа name, потом calories и напоследок id

'''

sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125,
}
print(sweet['name'],sweet['calories'],sweet['id'],sep='\n')
