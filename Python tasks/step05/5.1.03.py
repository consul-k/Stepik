num = int(input())
if num//1000+num//100%10 == num//10%10 + num%10:
    print(True)
else:
    print(False)
