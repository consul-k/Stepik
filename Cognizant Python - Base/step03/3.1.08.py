# Переменная request уже создана волшебным образом. Алон накосячил, но я в вас верю!
if isinstance(request[0], str) or isinstance(request[2], str):
    print('Алон, исправь строки на числа!')
else:
    print('Алон, всё нормально, это числа!')
