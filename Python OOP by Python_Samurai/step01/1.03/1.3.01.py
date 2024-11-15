class Button:
    def __init__(self, letter):
        self.letter = letter

# Создаем список экземпляров класса Button
lst = [Button(chr(i)) for i in range(ord('a'), ord('z') + 1)]
