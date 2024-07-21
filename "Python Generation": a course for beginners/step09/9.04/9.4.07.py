a = input()
if a.count('f'):
    if a.count('f') > 1:
        print(a.find('f'), a.rfind('f'))
    else:
        print(a.find('f'))
else:
    print('NO')
