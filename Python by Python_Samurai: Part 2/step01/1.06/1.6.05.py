import sys
lst = sys.stdin.readlines()
lst = [list(map(int, i.split())) for i in lst]

# продолжите решение здесь(в lst двумерный список)
result = [num for sublist in lst[::-1] for num in sublist[::-1] if num % 10 != 1]
print(*result)
