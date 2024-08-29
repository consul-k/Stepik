def quick_merge(lists):
    merged_list = []
    for lst in lists:
        merged_list.extend(lst)
    return sorted(merged_list)

n = int(input())
lists = []

for _ in range(n):
    lists.append(list(map(int, input().split())))

merged_list = quick_merge(lists)
print(*merged_list)
