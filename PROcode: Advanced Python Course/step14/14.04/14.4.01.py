try:
    with open("case_247.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("Архивный файл не найден! Немедленно сообщи директору!")
except PermissionError:
    print("Нет доступа к файлу! Запроси права у отдела безопасности!")
except IsADirectoryError:
    print("Ошибка: вместо файла указана папка! Проверь правильность пути!")
except Exception as e:
    print(e)
else:
    if not content.strip():
        print("Архивный файл пуст! Проверь правильность сохранения данных!")
    else:
        print(content)
finally:
    print("Операция завершена.")
