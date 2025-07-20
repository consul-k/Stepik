def make_dict(func):
    def wrapper(str1, str2):
        list1, list2 = func(str1, str2)
        return dict(zip(list1, list2))
    return wrapper

@make_dict
def split_words(str1, str2):
    return str1.split(), str2.split()
