s = input()

if s.isdigit():
    print("Это число")
elif s.isalpha():
    print("Это слово")
elif s.isalnum():
    print("Это буквы и цифры")
elif s.isspace():
    print("Это строка из пробельных символов")
else:
    print("Это что-то странное")
