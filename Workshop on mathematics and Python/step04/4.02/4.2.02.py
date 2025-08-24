def kaprekar_step(L):
    asc = int("".join(map(str, sorted(L))))
    desc = int("".join(map(str, sorted(L, reverse=True))))

    result = desc - asc
    
    return int(f"{result:04d}")
