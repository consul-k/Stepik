def create_chessboard(n):
    for i in range(n):
        row = ""
        for j in range(n):
            if (i + j) % 2 == 0:
                row += "X "
            else:
                row += "O "
        print(row)

n = int(input())
create_chessboard(n)
