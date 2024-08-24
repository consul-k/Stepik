stud1 = set([int(s) for s in input().split()])
stud2 = set([int(s) for s in input().split()])
stud3 = set([int(s) for s in input().split()])

s1_2 = stud1.intersection(stud2)
result = s1_2.difference(stud3)
result = sorted(result, reverse=True)

print(*result)
