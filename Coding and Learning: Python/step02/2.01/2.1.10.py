hours1 = int(input())
mins1 = int(input())

hours2 = int(input())
mins2 = int(input())

total_mins1 = hours1 * 60 + mins1
total_mins2 = hours2 * 60 + mins2

diff_mins = abs(total_mins1 - total_mins2)

print(diff_mins)
