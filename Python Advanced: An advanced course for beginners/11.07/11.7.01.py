def initialize_data():
    username = input()

    def update_data():
        nonlocal username
        username = input()
        print(username)

    update_data()
    print(username)

initialize_data()
