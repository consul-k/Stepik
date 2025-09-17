horses = (("Черный ворон", 45), ("Стальной конь", 50), ("Буря", 48))

horse_name = input()
distance = int(input())

for i in horses:
    if horse_name in i:
        speed = i[1]
        time_hours = distance / speed
        hours = int(time_hours)
        minutes = round((time_hours - hours) * 60)
        print(f"Лошадь {horse_name} пройдет {distance} км за {hours} часов и {minutes} минут.")
        break
else:
    print("Лошадь с таким именем не найдена.")
