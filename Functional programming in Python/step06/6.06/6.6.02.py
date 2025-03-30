def even_items(lst):
    return [j for i, j in enumerate(lst) if i%2!=0 and i!=0]
