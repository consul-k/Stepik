def del_value(tpl, value):
    return tuple(item for item in tpl if item != value)
