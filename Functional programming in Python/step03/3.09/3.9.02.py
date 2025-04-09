valid_categories = ['salad', 'soup', 'main_dish', 'drink', 'desert']

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
