# put your python code here
a = input()
if a[-1] == '?':
    print('Вопросительное')
elif a[-1] == '!':
    print('Восклицательное')
elif a[-1] == '.':
    print('Законченное')
elif a[-1] == ',':
    print('Незаконченное')
else:
    print('Неопределенное')
