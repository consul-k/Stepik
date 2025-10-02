lst = input().split(', ')
lst_filt = sorted(filter(lambda x: x.startswith('C') and len(x)>3, lst), key=lambda x: len(x))
print(lst_filt)
