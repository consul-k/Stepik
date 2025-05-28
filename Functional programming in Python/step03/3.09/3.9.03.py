valid_categories = ['salad', 'soup', 'main_dish', 'drink', 'desert']

tables = {}

def reserve_table(n, name, is_vip=False, order=None):
    if not tables.get(n):
        tables[n] = {'name': name, 'is_vip': is_vip, 'order': {}}

def delete_reservation(n):
    tables[n] = None

def make_order(n, **kwargs):
    if tables.get(n):
        order = tables[n]['order']
        for category, item in kwargs.items():
            if category in valid_categories:
                order[category] = item

def delete_order(*, number_table, delete_all=False, **kwargs):
    if tables.get(number_table):
        if delete_all:
            tables[number_table]['order'] = {}
        else:
            order = tables[number_table]['order']
            for category, should_delete in kwargs.items():
                if category in valid_categories and should_delete:
                    order.pop(category, None)
