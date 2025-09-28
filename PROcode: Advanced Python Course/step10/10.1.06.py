input_str = input()

achievements_list = [item.strip() for item in input_str.split(",")]

unique_achievements = set(achievements_list)

sorted_achievements = sorted(unique_achievements)

print(sorted_achievements)
