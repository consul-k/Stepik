def get_int(start_message, error_message, end_message):
    print(start_message)
    while True:
        user_input = input()
        try:
            value = int(user_input)
            print(end_message)
            return value
        except ValueError:
            print(error_message)
