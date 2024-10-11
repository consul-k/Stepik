def season(n):
    if n in [12,1,2,]:
        return 'зима'
    elif n in [3,4,5]:
        return 'весна'
    elif n in [6,7,8]:
        return 'лето'
    elif n in [9,10,11]:
        return 'осень'

print(season(int(input())))
