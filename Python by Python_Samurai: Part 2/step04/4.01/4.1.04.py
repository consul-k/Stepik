# вводные данные(не изменять)        
import sys
lst = [(x, int(y)) for i in sys.stdin.readlines() for x, y in [i.split()]]        

# продолжите решение здесь(в lst список кортежей)
for color, time in lst:
    match (color, time):
        case ("зеленый", 30):
            print("Да")
        case ("желтый", 5):
            print("Да")
        case ("красный", 25):
            print("Да")
        case _:
            print("Нет")
