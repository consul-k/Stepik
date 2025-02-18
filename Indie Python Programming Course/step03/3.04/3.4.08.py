a, b = input().lower(), input().lower()
if a[-1] == 'ь':
    if a[-2] == b[0]:
        print('Good')
    else:
        print('Bad')
elif a[-1] == b[0]:
    print('Good')
else:
    print('Bad')
