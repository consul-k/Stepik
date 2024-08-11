def get_days(month):
    days_in_month = {
        1: 31,
        2: 28,  # Невисокосный год
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    return days_in_month.get(month, "Неверный номер месяца")

print(get_days(int(input())))
