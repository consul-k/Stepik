income = int(input())
children = int(input())

per_capita = income / (1 + children)

if per_capita < 20000:
    status = "Бедность"
elif per_capita <= 50000:
    status = "Средний класс"
else:
    status = "Богатство"

print(status)
