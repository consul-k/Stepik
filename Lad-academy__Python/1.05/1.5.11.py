number = int(input())

previous_digit = number % 10
number //= 10
is_ordered = True

while number > 0:
    current_digit = number % 10
    if current_digit < previous_digit:
        is_ordered = False
        break
    previous_digit = current_digit
    number //= 10

if is_ordered:
    print("YES")
else:
    print("NO")
