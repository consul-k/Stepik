def reserve_table(n, name, is_vip=False):
    if not tables[n]:
        tables[n] = {'name': name, 'is_vip': is_vip}

def delete_reservation(n):
    tables[n] = None
