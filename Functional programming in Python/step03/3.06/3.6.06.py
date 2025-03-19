def print_goods(*args):
    cnt = 0
    for i in args:
        if type(i) == str and len(i) > 0:
            cnt += 1
            print(f'{cnt}. {i}')
    if cnt == 0:
        print('Нет товаров')
