stud1 = set([int(s) for s in input().split()])
stud2 = set([int(s) for s in input().split()])
stud3 = set([int(s) for s in input().split()])

scores = {0,1,2,3,4,5,6,7,8,9,10}

result = scores - stud1 - stud2 - stud3
result = sorted(result)

print(*result)
