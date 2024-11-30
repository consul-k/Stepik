def check_duplicates(surnames):
    surname_list = surnames.split()
    surname_count = {}

    for surname in surname_list:
        if surname in surname_count:
            surname_count[surname] += 1
        else:
            surname_count[surname] = 1

    for count in surname_count.values():
        if count > 1:
            return 1
    return 0

surnames = input()
print(check_duplicates(surnames))
