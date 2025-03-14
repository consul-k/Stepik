def show_list(include_quantities=True):
    if include_quantities:
        for item in shopping_list:
            print(f'{shopping_list[item]}x{item}')
    else:
        for item in shopping_list:
            print(item)
