participants = {1, 2, 3, 4, 5}

new_members = input().split()
new_members = set(map(int, new_members))
participants.update(new_members)
print("После добавления участников:", participants)

remove_number = int(input())
participants.remove(remove_number)
print(f"После удаления участника с номером {remove_number}:", participants)

discard_number = int(input())
participants.discard(discard_number)
print(f"После удаления участника с номером {discard_number} (метод discard):", participants)

removed = participants.pop()
print(f"Удалён случайный участник с номером {removed}.")
print("Оставшиеся участники:", participants)

participants.clear()
print("После очистки списка участников:", participants)
