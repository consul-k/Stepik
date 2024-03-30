def avg(one, two, three):
    if one >= two and one <= three:
        return one
    elif two >= one and two <= three:
        return two
    elif three >= two and three <= one:
        return three

print(avg(int(input()), int(input()), int(input())))
