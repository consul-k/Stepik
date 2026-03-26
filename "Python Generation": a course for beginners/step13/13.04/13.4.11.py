def quick_merge(lists):
    result = []
    while any(lists):
        min_val = float('inf')
        min_idx = -1
        
        for i, lst in enumerate(lists):
            if lst and lst[0] < min_val:
                min_val = lst[0]
                min_idx = i

        result.append(min_val)
        lists[min_idx].pop(0)
    
    return result

n = int(input())
lists = []

for _ in range(n):
    line = input().strip()
    if line:
        lists.append(list(map(int, line.split())))
    else:
        lists.append([])

merged = quick_merge(lists)

print(*merged)
