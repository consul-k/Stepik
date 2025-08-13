s = list(map(int, input().split()))
a = s[0]
b = s[1]

for i in range(a,b+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
