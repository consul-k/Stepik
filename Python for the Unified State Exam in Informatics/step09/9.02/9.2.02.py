def odd_factorial(n: int) -> int:
    if n <= 1:
        return 1
    if n % 2 == 0:
        return odd_factorial(n - 1)
    return n * odd_factorial(n - 2)
