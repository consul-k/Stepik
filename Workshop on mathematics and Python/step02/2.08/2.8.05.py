#your code
import os

a = input()

if os.path.exists(a):
    if os.path.isfile(a):
        with open(a, encoding='utf-8') as f:
            print(f'CONTENT:\n{f.read()}')
    else:
        print('ERROR:\nЭто каталог, а не файл')
else:
    print('ERROR:\nФайл не существует')
