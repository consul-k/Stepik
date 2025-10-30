all_participants = input().strip()
passed_participants = input().strip()

all_set = set(name.strip() for name in all_participants.split(','))
passed_set = set(name.strip() for name in passed_participants.split(','))

not_passed = all_set - passed_set
both = all_set & passed_set
all_union = all_set | passed_set
symmetric_diff = all_set ^ passed_set

print(f"1. Кто был на шоу, но не прошел первый тур: {', '.join(sorted(not_passed))}")
print(f"2. Кто пришел на шоу и прошел первый тур: {', '.join(sorted(both))}")
print(f"3. Все, кто хотя бы один раз был на шоу: {', '.join(sorted(all_union))}")
print(f"4. Кто пришел на шоу, но не прошел тур, и наоборот: {', '.join(sorted(symmetric_diff))}")
