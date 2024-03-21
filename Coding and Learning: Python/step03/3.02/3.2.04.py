a = int(input())
a1 = int(input())

b = int(input())
b1 = int(input())

common_denom = a1 * b1
a_common = a * b1
b_common = b * a1

if a_common > b_common:
    print("1st > 2nd")
elif a_common < b_common:
    print("1st < 2nd")
else:
    print("1st = 2nd")
