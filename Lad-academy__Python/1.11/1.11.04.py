def square(a):
    p = 4 * a
    s = a * a
    d = (a ** 2 + a ** 2) ** 0.5

    k = (p, s, d)

    return k

print(square(int(input())))
