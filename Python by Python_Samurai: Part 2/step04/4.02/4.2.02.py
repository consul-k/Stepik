# вводные данные(не изменять)
lst = _

# продолжите решение здесь(в lst вложенные списки)
for sub_lst in lst:
    match sub_lst:
        case [str(), _, _, list(), *_]:
            print(sub_lst)
        case [_, _, _, dict(), *_, tuple()]:
            print(sub_lst)
