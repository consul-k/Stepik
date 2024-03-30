def edges_sum(a, b, c):
    return 4 * (a + b + c)

a, b, c = [int(i) for i in input().split()] 

print(edges_sum(a, b, c))
