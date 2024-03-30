def frame(a, b):
    for i in range(a):
        if i == 0 or i == a - 1:
            print("+", "-" * (b - 2), "+", sep="")
        else:
            print("|", " " * (b - 2), "|", sep="")

frame(int(input()), int(input()))
