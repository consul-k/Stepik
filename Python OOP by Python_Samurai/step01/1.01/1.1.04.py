# вводные данные
class Number:
    x = None

# продолжите решение здесь
lst = list(map(int, input().split()))
Number.x = max(lst)
