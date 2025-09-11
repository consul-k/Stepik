victor_area = int(input())
mikhail_area = int(input())

if victor_area > mikhail_area:
    print("Виктор охраняет больше")
elif mikhail_area > victor_area:
    print("Михаил охраняет больше")
else:
    print("Они охраняют одинаковые участки")

if victor_area <= 100 and mikhail_area <= 100:
    print("Ни у кого из стражей нет участка больше 100 квадратных метров")
