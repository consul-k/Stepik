import random

number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = int(input("Угадай число от 1 до 100: "))
    if guess < number:
        print("Слишком мало")
    elif guess > number:
        print("Слишком много")

print("Вы угадали!")
