def calculate_days(x, y):
    days = 1
    distance = x

    while distance < y:
        distance += distance * 0.1
        days += 1

    return days

x = float(input())
y = float(input())

days = calculate_days(x, y)
print(days)
