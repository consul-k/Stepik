def create_square_list(n):
    return [i**2 for i in range(1, n + 1)]

n = int(input())
result = create_square_list(n)
print(result)
