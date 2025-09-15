temps = list(map(int, input().split()))

def multiply_min_max(min_val, max_val):
    return min_val * max_val

min_temp = min(temps)
max_temp = max(temps)

result = multiply_min_max(min_temp, max_temp)
print(result)
