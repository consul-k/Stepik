def get_info_about_object(n):
    res = dir(n)
    print(res)
    print(f'Всего у объекта {len(res)} атрибутов и методов')
