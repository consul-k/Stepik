def process_queue(client_names):
    # Если список пуст, ничего не делаем
    if not client_names:
        return

    # Перебираем клиентов в очереди
    while client_names:
        # Берем последнего клиента из списка (первого в очереди)
        current_client = client_names.pop()
        print(f"Клиент {current_client} пройдите к стойке!")

        # Если остались клиенты в очереди, выводим их имена
        if client_names:
            remaining_clients = ','.join(reversed(client_names))
            print(f"{remaining_clients} ожидайте!")

# Получаем список имен клиентов из ввода пользователя
client_input = input()
client_list = client_input.split()

# Обрабатываем очередь
process_queue(client_list)
