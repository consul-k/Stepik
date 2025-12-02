commands_input = input().strip()
commands_list = commands_input.split()

print(commands_list)
print(f"Всего команд: {len(commands_list)}")
print(f"Уникальных команд: {len(set(commands_list))}")

command_count = {}
for command in commands_list:
    command_count[command] = command_count.get(command, 0) + 1

max_count = 0
most_common = ""
for command, count in command_count.items():
    if count > max_count:
        max_count = count
        most_common = command

print(f"Чаще всего используется: {most_common}")
