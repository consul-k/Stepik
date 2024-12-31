right_answer = tuple(input().split())
person_answer = tuple(input().split())
res = 0

for i in right_answer:
    if i in person_answer:
        res += 1
print(res)
