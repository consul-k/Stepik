def generate_even_odd_dict(n):
    return {i: ("even" if i % 2 == 0 else "odd") for i in range(1, n + 1)}

n = int(input())
result = generate_even_odd_dict(n)
print(result)
