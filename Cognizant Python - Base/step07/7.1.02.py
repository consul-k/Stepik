def slice_generator(lst: list, slice_size: int):     
    for i in range(0, len(lst), slice_size):
        yield lst[i:i + slice_size]


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# код выше менять нельзя, просто допишите код, чтобы вывести список частями по три элемента.
gen = slice_generator(my_list, 3)
print(next(gen))
print(next(gen))
print(next(gen))
