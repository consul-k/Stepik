all_checks = set(map(int, input().split()))
client_check = int(input())

if client_check in all_checks:
    print("Осуществляем возврат")
else:
    print("Такой суммы нет")
