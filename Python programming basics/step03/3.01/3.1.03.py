age = int(input())
if age < 12:
    print("Фильмы для детей")
elif 12 <= age < 16:
    print("Подростковые фильмы")
elif 16 <= age < 18:
    print("Фильмы для старших подростков")
elif age >= 18:
    print("Фильмы для взрослых")
