scroll1 = input().split()
scroll2 = input().split()

set1 = set(scroll1)
set2 = set(scroll2)
common = frozenset(set1 & set2)

print(f"Уникальные руны первого свитка: {sorted(set1)}")
print(f"Уникальные руны второго свитка: {sorted(set2)}")
print(f"Защищённый свиток (общие руны): frozenset({sorted(common)})")
