def quick_power(a, n):
    print(f"State: a={a}, n={n}")
    
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_power = quick_power(a, n // 2)
        return half_power * half_power
    else:
        return quick_power(a, n - 1) * a
