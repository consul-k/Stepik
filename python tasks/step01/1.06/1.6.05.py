def prostye_chisla_do_n(n):
    if n >= 1:
        print(1)
    for num in range(2, n + 1):
        prostoe = True
        for delitel in range(2, int(num ** 0.5) + 1):
            if num % delitel == 0:
                prostoe = False
                break
        if prostoe:
            print(num)

n = int(input())
prostye_chisla_do_n(n)
