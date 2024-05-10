# вводные данные
foto = [
    [['B', 'W', 'Y'], ['C', 'Y', 'M'], ['M', 'B', 'W']],
    [['B', 'B', 'W'], ['W', 'W', 'B'], ['W', 'B', 'W']],
    [['C', 'B', 'W'], ['B', 'W', 'Y'], ['B', 'W', 'B']],
    [['W', 'B', 'W'], ['B', 'W', 'B'], ['B', 'W', 'B']],
    [['C', 'B', 'Y'], ['B', 'C', 'Y'], ['Y', 'W', 'B']]
]

# продолжить решение здесь
for photo in foto:
    is_color = False
    for row in photo:
        for pixel in row:
            if pixel in ['C', 'Y', 'M']:
                is_color = True
                break
        if is_color:
            break
    print("Цветная" if is_color else "Ч/Б")
