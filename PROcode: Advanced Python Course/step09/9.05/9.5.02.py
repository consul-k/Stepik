group1 = set(input().split(', '))
group2 = set(input().split(', '))

if group1.issubset(group2):
    print("Первая группа - подмножество второй.")
elif group2.issubset(group1):
    print("Вторая группа - подмножество первой.")
elif group1.isdisjoint(group2):
    print("Группы не пересекаются.")
else:
    print("Группы пересекаются, но ни одна не является подмножеством другой.")
