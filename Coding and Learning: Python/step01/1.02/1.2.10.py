string1 = input()
string2 = input()

num1 = int(input())
num2 = int(input())

for _ in range(num1):
    print(string1 + ' ' + string2)
print(len(string1 + ' ' + string2)*num2)
