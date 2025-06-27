N = int(input())

grades = tuple(int(input()) for i in range(N))

average = sum(grades) / N

above_or_equal_avg = tuple(grade for grade in grades if grade >= average)

print(grades)
print(f"{average:.2f}")
print(above_or_equal_avg)
