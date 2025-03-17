def reserve_table(n, name):
    if not tables[n]:
        tables[n] = name

def delete_reservation(n):
    tables[n] = None
