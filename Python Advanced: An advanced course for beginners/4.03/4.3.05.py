def create_initials(name, surname, patronymic):
    initials = surname[0].upper() + name[0].upper() + patronymic[0].upper()
    print(initials)
