def check_number(k):
    if 24 <= k <= 25:
        print("ПОПАЛ")
    elif k >= 26:
        print("ПЕРЕЛЕТ")
    elif 0 < k < 24:
        print("НЕДОЛЕТ")
    else:
        print("МАЗИЛА")

k = int(input())
check_number(k)
