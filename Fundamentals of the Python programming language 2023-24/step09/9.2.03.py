numbers = list(map(int, input().split()))

seen_numbers = set()

for number in numbers:
    if number in seen_numbers:
        print("YES")
    else:
        print("NO")
        seen_numbers.add(number)
