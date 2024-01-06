'''

У Машеньки день рождения, и она планирует отправиться в парк с единорогами. 
В парке идёт акция, приведи 5 друзей и получишь шапку-единорожку. Машенька любит разные весёлые шапки, поэтому пригласила 5 друзей. 
Но в последний момент один из её друзей не смог прийти, и она решила пригласить вас на свой день рождения. Помогите Машеньке обрести шапку-единорожку.
Задание:

    Создайте пустой класс Holiday (используйте pass внутри класса).
    Создайте экземпляр friends.
    Создайте 5 атрибутов для экземпляра friends, с именами name1, name2...name5 со значениями 'Sveta', 'Katya', 'Lena', 'Natasha', 
    'Leonardo DiCaprio' соответственно.
    Так как 'Leonardo DiCaprio' не смог прийти, Машенька приглашает вас на свой ДР. 
    Измените атрибут name5 на своё имя, или можете использовать любое другое имя.
    Часть кода уже написана, вам нужно лишь сделать то, что написано в задании.

Sample Input:

Sample Output:

Sveta
Katya
Lena
Natasha

'''

# Напишите ваш код:
class Holiday:
    pass

friends = Holiday()
friends.name1 = 'Sveta'
friends.name2 = 'Katya'
friends.name3 = 'Lena'
friends.name4 = 'Natasha'
friends.name5 = 'Bro'
# Код ниже пожалуйста не удаляйте, ради Машеньки!
for i in friends.__dict__:
    if i != 'name5':
        print(getattr(friends, i))
    elif i == 'name5' and getattr(friends, i) == 'Leonardo DiCaprio':
        raise AttributeError('Машенька хочет увидеть вас на ДР')
    else:
        pass
