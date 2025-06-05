def decrypt_message(encrypted):
    reversed_str = encrypted[::-1]

    with_spaces = reversed_str.replace("_", " ")

    decrypted = ""
    for char in with_spaces:
        if char == "А":
            decrypted += "Я"
        elif char == "а":
            decrypted += "я"
        elif 'Б' <= char <= 'Я' or 'б' <= char <= 'я':
            decrypted += chr(ord(char) - 1)
        else:
            decrypted += char

    return decrypted

encrypted_input = input().strip()

decrypted = decrypt_message(encrypted_input)

print(decrypted)
if "АРМИЯ" in decrypted:
    print("Чапаев, приказ выполнен!")
else:
    print("Чапаев, действуй быстро, шифр не раскрыт!")
