stud1 = set([int(s) for s in input().split()])
stud2 = set([int(s) for s in input().split()])
stud3 = set([int(s) for s in input().split()])

result = stud3.difference(stud2, stud1)
result = sorted(result, reverse=True)

print(*result)
