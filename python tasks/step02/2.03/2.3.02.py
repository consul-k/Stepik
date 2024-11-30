N = int(input())

students = []

for _ in range(N):
    data = input().split()
    surname = data[0]
    score = int(data[1])
    students.append((surname, score))

passing_score = int(input())

for surname, score in students:
    if score >= passing_score:
        print(surname)
