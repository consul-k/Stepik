str1 = input()
str2 = input()
if len(str1) < 7:
    print('Short')
elif str1 != str2:
    print('Difference')
elif len(str1) > 7 and str1 == str2:
    print('OK')
