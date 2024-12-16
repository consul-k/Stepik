N = int(input())
K = int(input())

apples_per_student = K // N

students_with_less_apples = N - (K % N)

if students_with_less_apples == N:
    students_with_less_apples = 0

print(students_with_less_apples)
