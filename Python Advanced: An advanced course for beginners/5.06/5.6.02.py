message_tuple = ('Агент', 'Джей,', 'твоя', 'следующая', 'миссия')

secret_word = input()

message_tuple += (secret_word,)

full_message = ' '.join(message_tuple)

print("Полное сообщение:", full_message)
