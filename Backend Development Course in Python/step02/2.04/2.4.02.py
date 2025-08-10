str1 = input()
str2 = input()

if all(char in str1 for char in str2):
    print("Да, первая строка содержит все символы второй строки")
else:
    print("Нет, первая строка не содержит все символы второй строки")
