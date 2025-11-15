def access_control(required_level):
    levels = {'guest': 0, 'manager': 1, 'admin': 2}
    
    def decorator(func):
        def wrapper(user_level):
            if user_level not in levels:
                return "Ошибка: доступ запрещен"
            
            if levels[user_level] >= levels[required_level]:
                return func(user_level)
            else:
                return "Ошибка: доступ запрещен"
        return wrapper
    return decorator

@access_control('manager')
def delete_data(user_level):
    return f"✅ Данные успешно удалены (пользователь: {user_level})"
