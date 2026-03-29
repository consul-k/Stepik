def is_valid_password(password):
    parts = password.split(':')
    if len(parts) != 3:
        return False

    a, b, c = map(int, parts)

    if str(a) != str(a)[::-1]:
        return False

    if b < 2 or any(b % i == 0 for i in range(2, int(b**0.5) + 1)):
        return False

    if c % 2 != 0:
        return False

    return True

psw = input()

print(is_valid_password(psw))
