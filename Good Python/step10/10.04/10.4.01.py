import random

i = 0
while True:
    random.seed(i)
    for j in range(20):
        if random.randrange(2):
            break
    else:
        print(i)
        break
    i += 1
