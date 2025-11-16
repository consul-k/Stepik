decryption_dict = eval(input())

encrypted_string = input()

codes = encrypted_string.split()

decrypted_words = [decryption_dict[code] for code in codes]

result = ' '.join(decrypted_words)

print(result)
