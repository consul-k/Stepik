participants = {1, 2, 3, 4, 5}

# Ввод новых участников
new_members = input().split()  # Ввод: 6 7 8 9
new_members = set(map(int, new_members))
participants.update(new_members)
print("После добавления участников:", participants)

# Удаление участника методом remove()
remove_number = int(input())  # Ввод: 3
participants.remove(remove_number)
print(f"После удаления участника с номером {remove_number}:", participants)

# Удаление участника методом discard()
discard_number = int(input())  # Ввод: 7
participants.discard(discard_number)
print(f"После удаления участника с номером {discard_number} (метод discard):", participants)

# Удаление случайного участника методом pop()
removed = participants.pop()
print(f"Удалён случайный участник с номером {removed}.")
print("Оставшиеся участники:", participants)

# Очистка списка участников
participants.clear()
print("После очистки списка участников:", participants)
