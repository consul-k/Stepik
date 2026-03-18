day = int(input())
current_weight = float(input())

total_loss = 100 - 88
daily_loss = total_loss / 60

target_weight = 100 - (day * daily_loss)

if current_weight <= target_weight:
    print("Все идет по плану")
else:
    print("Что-то пошло не так")

print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight} кг, ЦЕЛЬ по ВЕСУ = {target_weight} кг")
