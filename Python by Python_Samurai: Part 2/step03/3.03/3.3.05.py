# вводные данные              
athletes = (
            {'Дамблдор', 'Егор', 'Максим', 'Конь', 'Владимир', 'Никита', 'Ринат'},
            {'Флеш', 'Вадим', 'Никита', 'Николай', 'Дипси', 'Олег', 'Александр'},
            {'Вучич', 'Егор', 'Николай', 'Конь', 'Дмитрий', 'Шишига', 'Тимофей', 'Артем'}
)

# продолжите решение здесь
unique_athletes = set()
updated_athletes = []

for race in athletes:
    updated_race = race - unique_athletes
    unique_athletes |= race
    updated_athletes.append(updated_race)

athletes = tuple(updated_athletes)
