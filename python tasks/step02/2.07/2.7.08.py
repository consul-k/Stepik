colors = input().split()

target_color = input()

target_count = colors.count(target_color)

total_count = len(colors)

probability = (target_count / total_count) * 100
probability = int(probability)

print(str(probability)+'%')
