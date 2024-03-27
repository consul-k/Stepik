def count_operations(n):
    if n == 1:
        return 0
    
    if n % 2 == 1:
        return count_operations(n * 3 + 1) + 1
    
    else:
        return count_operations(n // 2) + 1

n = int(input())

print(count_operations(n))
