'''

    Создайте пустой класс Pokemon (используйте pass).
    Создайте экземпляр pokemons класса Pokemon.
    С помощью setattr(), добавьте в экземпляр, 4 атрибута: pikachu, scyther, gyarados, gengar. Значения у всех атрибутов будет пустая строка, например pikachu = "". Можно использовать списки и циклы, или как вам удобней.
    С помощью hasattr(), сделайте проверку, есть ли в экземпляре атрибут: lapras, pikachu, alakazam. Результат проверки напишите на отдельной строке, соответственно перечисленным атрибутам (см. пример ниже).

 

# напоминашка
hasattr(object, name)
# object - объект, у которого нужно проверить наличие атрибута (класс, экземпляр).
# name - атрибут, наличие которого нужно проверить.

Sample Input:

Sample Output:

False
True
False

'''

class Pokemon:
    pass

pokemons = Pokemon()
setattr(pokemons, 'pikachu', '')
setattr(pokemons, 'scyther', '')
setattr(pokemons, 'gyarados', '')
setattr(pokemons, 'gengar', '')

print(hasattr(pokemons, 'lapras'))
print(hasattr(pokemons, 'pikachu'))
print(hasattr(pokemons, 'alakazam'))
