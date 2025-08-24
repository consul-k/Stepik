def numerics(n):
    return [int(i) for i in str(n)]

def kaprekar_step(L):
    asc = int("".join(map(str, sorted(L))))
    desc = int("".join(map(str, sorted(L, reverse=True))))
    
    result = desc - asc
    
    return int(f"{result:04d}")

def kaprekar_loop(n):
    print(n)
    while n != 6174:
        n = kaprekar_step(numerics(n))
        print(n)
