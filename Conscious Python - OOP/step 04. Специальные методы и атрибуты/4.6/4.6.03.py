'''

Машенька мечтает слетать в Казахстан к своему другу Васе, помогите ей осуществить мечту. Часть кода уже написана. 
Вам нужно лишь создать подходящий метод или методы.

Sample Input:

Sample Output:

Ура, Маша летит в Казахстан!

'''

class Country:
    country = ('Russia', 'Ukraine', 'Belarus', 'Kazakhstan', 'Other')

    # создайте метод(ы)
    def __iter__(self):
        return iter(self.country)

# код ниже, не меняйте, ради Машеньки
country_is = Country()
for i in country_is:
    if i == 'Kazakhstan':
        print(f'Ура, Маша летит в Казахстан!')
