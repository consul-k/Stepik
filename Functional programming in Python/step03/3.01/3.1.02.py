def is_adult(age):
    if age >= 18:
        return True
    else:
        return False


a = int(input())
if is_adult(a):
    print('Ух какой большой')
else:
    print('Подрасти еще, сынок')
