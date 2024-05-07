start, end = map(int, input().split())
numbers = range(start, end + 1) if start < end else range(start, end - 1, -1)
result = [*numbers]
print(result)
