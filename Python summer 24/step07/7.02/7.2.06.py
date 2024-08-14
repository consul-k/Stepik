def merge(list1, list2):
    return sorted(list1 + list2)

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

print(merge(list1, list2))
