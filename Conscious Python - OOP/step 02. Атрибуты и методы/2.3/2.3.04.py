'''

Машенька увлеклась изучением коктейлей, и используя книгу, решила угостить вас её коктейлем. 
Правда Машенька не знала, что это книга для начинающих ведьмочек. Напишите программу, чтобы узнать, какие ингредиенты выпадут именно вам.
Задание:

    Часть кода уже написана
    Создайте класс Magic
    Создайте атрибут ingredients со значением [magic_ing[i] for i in lucky]. Таким образом создастся список из трёх рандомных ингредиентов для коктейля.
    Создайте экземпляр my_cocktail от класса Magic (не забудьте скобки).
    С помощью getattr(), используя экземпляр, выведите на экран значение атрибута ingredients (не забудьте про кавычки).
    Нажмите кнопку "Запустить код", таким образом вы увидите ингредиенты, которые Машенька приготовила именно для вас и вашего коктейля.
    Закомментируйте, всё что вы сделали в пункте 5 задания. Закомментировать, значит поставить # перед кодом.
    Выведите на экран текст: "Спасибо, Машенька!" и нажмите кнопку "Отправить".

К сожалению, на Степике нет кнопки - "любой ответ правильный", поэтому необходимо выполнить пункт 7, чтобы пройти задание. Не удаляйте код, 
просто закомментируйте его, чтобы можно было увидеть ваше решение. И по желанию, напишите в комментарии, какие ингредиенты выпали именно вам, 
возможно это поднимет кому-то настроение. Спасибо!

Sample Input:

Sample Output:

Спасибо, Машенька!

'''

import random
lucky = [random.randint(0, 29), random.randint(0, 29), random.randint(0, 29)]
magic_ing = ["Черные коты", "Лягушачьи глаза", "Паутина", "Корень мандрагоры",
             "Жабий язык", "Женский волос", "Крысы", "Любовное зелье", "Кровь дракона", 
             "Пепел отрока","Чертополох", "Пыльца беладонны", "Черная свеча", 
             "Сердце ворона", "Собачий клык", "Масло лунного света", "Костыли ведьмы", 
             "Подземный гриб","Крыло летучей мыши","Ядовитый плющ", "Перо ворона", 
             "Камень чародея", "Слезы совы","Горсть звездной пыли","Волшебный кристалл", 
             "Костер из драконьих костей","Зелье бессмертия","Черная роза", 
             "Древний свиток заклинаний", "Ключ от врат ада"]

# ниже ваш код:
class Magic:
    ingredients = [magic_ing[i] for i in lucky]
    
my_cocktail = Magic()
#print(getattr(my_cocktail, 'ingredients', False))
#['Подземный гриб', 'Лягушачьи глаза', 'Пыльца беладонны']

print('Спасибо, Машенька!')
