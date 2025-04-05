def print_to(n):
    if n > 0:
        print_to(n-1)
        print(n)
