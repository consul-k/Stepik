def del_from_tuple(tpl, elem):
    lst = list(tpl)
    if elem in tpl:
        lst.remove(elem)
    return tuple(lst)

tpl = list(map(int, input().split(',')))
elem = int(input())

print(del_from_tuple(tpl, elem))
