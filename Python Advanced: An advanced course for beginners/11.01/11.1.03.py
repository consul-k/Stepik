def political_debate(*arguments, key_argument):
    print("🎙 Политический дебат начинается!")
    print("📢 Политики приводят доводы:")
    for arg in arguments:
        print(f"- {arg}")
    print(f"🔥 Ключевой аргумент: {key_argument}")
    print("✅ Дебаты завершены!")
