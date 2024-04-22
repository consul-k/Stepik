def day_of_week(day_number):
    days = ["вторник", "среда", "четверг", "пятница", "суббота", "воскресенье", "понедельник"]
    return days[(day_number - 1) % 7]

day = int(input())
print(day_of_week(day))
