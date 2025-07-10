N = int(input())

A = set(input().split())

M = int(input())
B = set(input().split())

# Проверка условий
print(f"A is subset of B? {A.issubset(B)}")
print(f"B is superset of A? {B.issuperset(A)}")
print(f"A and B are disjoint? {A.isdisjoint(B)}")
