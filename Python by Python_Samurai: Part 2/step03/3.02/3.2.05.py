# продолжите решение здесь
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

result_set = set1.union(set2)

if len(result_set) == 20 and min(result_set) == 1 and max(result_set) == 20:
    print("ДА")
else:
    print("НЕТ")
