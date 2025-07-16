match1 = input()
match2 = input()

set1 = set(map(str.strip, match1.split(',')))
set2 = set(map(str.strip, match2.split(',')))

common = sorted(set1 & set2)
only_in_match1 = sorted(set1 - set2)
only_in_match2 = sorted(set2 - set1)

print(f"Общие достижения: {common}")
print(f"Достижения только в матче 1: {only_in_match1}")
print(f"Достижения только в матче 2: {only_in_match2}")
