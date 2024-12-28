parasites = ["Эээ", "Типа", "Короче", "Ну", "Как бы"]
a = input().lower()
for word in parasites:
    if word.lower() in a:
        print('Слова паразиты обнаружены')
        break
else:
    print('Слов паразитов не обнаружено')
