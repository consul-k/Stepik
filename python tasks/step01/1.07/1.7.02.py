def check_string(s):
    if s.isalpha():
        print("Это слово")
    elif s.isdigit():
        print("Это целое число")
    else:
        print("Обычная строка")

s = input()
check_string(s)
