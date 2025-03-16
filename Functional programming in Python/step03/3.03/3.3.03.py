def is_table_free(n):
    if tables[n]:
        return False
    else:
        return True

def get_free_tables():
    return [i for i in tables if not tables[i]]
