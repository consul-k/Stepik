words = input().split()
num = int(input())
result = [i for i in words if len(i) == num]
print(result)
