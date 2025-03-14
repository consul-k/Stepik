shopping_list = {}

def add_item(item, count=1):
    if item not in shopping_list:
        shopping_list[item] = count
    else:
        shopping_list[item] += count
