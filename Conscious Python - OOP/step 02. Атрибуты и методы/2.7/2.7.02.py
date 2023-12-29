'''

Вводные данные:

У Васи день рождения, и три друга (Masha, Nikita, Lena) придут с подарком. Вася любит красный цвет.

    Masha - подарит красную ручку ("pen", "red")
    Nikita - подарит красную футболку ("t-shirt", "red")
    Lena - подарит красный мяч ("ball", "red")

Задача:

    Создайте класс Present и объявите метод __init__. В аргументах __init__ укажите (self, present, color).
    Метод __init__ создаёт два атрибута present и color, и присваивает им значения аргументов present, color соответственно. 
    Объявите в методе создание этих атрибутов.
    Создайте три экземпляра (Masha, Nikita, Lena) и создайте у них атрибуты present, color соответственно тем подаркам, которые они подарят. 
    Например Masha подарит, present - "pen", color - "red".
    Выведите на экран значения атрибутов у каждого экземпляра, согласно примеру ниже.

Sample Input:

Sample Output:

Маша подарила: pen, цвета: red
Никита подарил: t-shirt, цвета: red
Лена подарила: ball, цвета: red

'''

class Present:
    def __init__(self, present, color):
        self.present = present
        self.color = color

Masha = Present("pen", "red")
Nikita = Present("t-shirt", "red")
Lena = Present("ball", "red")

print(f'Маша подарила: {Masha.present}, цвета: {Masha.color}')
print(f'Никита подарил: {Nikita.present}, цвета: {Nikita.color}')
print(f'Лена подарила: {Lena.present}, цвета: {Lena.color}')
