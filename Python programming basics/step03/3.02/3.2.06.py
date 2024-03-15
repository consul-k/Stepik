def pyramid_numbers(n):
    numbers = []
    k = 1
    while True:
        pyramid_num = k * (k + 1) * (2*k + 1) // 6
        if pyramid_num >= n:
            break
        numbers.append(pyramid_num)
        k += 1
    return numbers

n = int(input(""))
print(*pyramid_numbers(n))
