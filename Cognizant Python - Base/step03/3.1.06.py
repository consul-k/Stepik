first_line = input()
second_line = input()

opening_time, closing_time, day_off = first_line.split()
current_time, current_day = second_line.split()

opening_time = int(opening_time)
closing_time = int(closing_time)
current_time = int(current_time)

if current_day == day_off:
    print("Закрыто")  # Сегодня выходной
elif current_time < opening_time or current_time >= closing_time:
    print("Закрыто")  # Время не соответствует графику работы
else:
    print("Открыто")  # Магазин работает
