def simulate_battle():
    health = 100
    hit_count = 0

    print(f"Уровень здоровья: {health}")

    while health > 0:
        try:
            damage = int(input())
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        health -= damage
        hit_count += 1

        if health > 0:
            print(f"Уровень здоровья: {health}")
        else:
            print('Игра окончена.')

    print(f"Количество ударов, которые ваш персонаж героически выдержал = {hit_count-1}")
    print(f"Удар № {hit_count} был критическим")

simulate_battle()
