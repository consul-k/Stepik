def tribonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n == 3:
        return [1, 1, 1]
    else:
        seq = [1, 1, 1]
        for i in range(3, n):
            next_num = seq[i-1] + seq[i-2] + seq[i-3]
            seq.append(next_num)
        return seq

n = int(input())
sequence = tribonacci(n)
print(*sequence)
