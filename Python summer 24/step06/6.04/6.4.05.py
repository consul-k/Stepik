def is_valid_octet(octet):
    return octet.isdigit() and 0 <= int(octet) <= 255

ip_address = input()

octets = ip_address.split('.')

if len(octets) != 4:
    print("НЕТ")
else:
    if all(is_valid_octet(octet) for octet in octets):
        print("ДА")
    else:
        print("НЕТ")
