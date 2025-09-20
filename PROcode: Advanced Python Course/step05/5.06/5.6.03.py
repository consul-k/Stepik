old_passwords = ('virus', 'antivirus', 'zombie', 'virus', 'bio', 'zombie', 'bio', 'virus', 'biohazard', 'virus', 'biohazard')

new_pass1 = input()
new_pass2 = input()

passwords_list = list(old_passwords)

passwords_list.append(new_pass1)
passwords_list.append(new_pass2)

unique_passwords = []
for p in passwords_list:
    if p not in unique_passwords:
        unique_passwords.append(p)

unique_passwords.sort(key=len)

new_passwords = tuple(unique_passwords)

print("Старый кортеж паролей:", old_passwords)
print("Новый кортеж паролей:", new_passwords)
