summa = sum(map(int, data[1]))  # количество товаров
price = round(sum(map(float, data[3])) / 3)  # средняя цена
description = ', '.join(data[2])  # описание товаров

print(f'''Название: {data[0]}
Количество: {summa}
Описание товара: {description}
Средняя цена: {price}
Отзыв: {data[4]}''')
