weekdays = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

days = ((day, weekdays[(day - 1) % 7]) for day in range(1, 366))

for day in range(77):
    print(next(days))
