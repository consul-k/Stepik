h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

start_minutes = h1 * 60 + m1
end_minutes = h2 * 60 + m2

for minutes in range(start_minutes, end_minutes + 1):
    hours = minutes // 60
    mins = minutes % 60
    print(f"{hours:02d}:{mins:02d}")
