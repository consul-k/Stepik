def accumulate_until_target(incomes, target):
    total = 0
    index = 0

    while index < len(incomes) and total < target:
        total += incomes[index]
        index += 1

    print(total)

    if total >= target:
        print("Цель достигнута")
    else:
        print("Цель не достигнута")

incomes_input = input()
target_input = input()

incomes = list(map(int, incomes_input.split()))
target = int(target_input)

accumulate_until_target(incomes, target)
