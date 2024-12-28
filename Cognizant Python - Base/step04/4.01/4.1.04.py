import random

# Ваш код для создания программы напишите ниже:
random_number = random.randint(1, 3)
cnt = 1

while random_number != 3:
    random_number = random.randint(1, 3)
    cnt += 1
else:
    print(cnt)
