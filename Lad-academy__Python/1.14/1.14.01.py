def slicer(tup, elem):
    if elem not in tup:
        return ()

    first_index = tup.index(elem)

    try:
        second_index = tup.index(elem, first_index + 1)
        return tup[first_index:second_index + 1]
    except ValueError:
        return tup[first_index:]

a = tuple(map(int, input().split(',')))
s = int(input())
print(slicer(a, s))
