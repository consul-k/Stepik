def calculate_area(width, height):
    return width * height

def display_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"📏 Площадь помещения: {result} м²")
        return result
    return wrapper
