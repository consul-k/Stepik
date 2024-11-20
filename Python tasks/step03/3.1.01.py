coins = list(map(int, input().split())) # ввод строки с годами выпуска монет, разделенной пробелами
check = sorted(coins)
if check == coins:
    print(True)
else:
    print(False)
