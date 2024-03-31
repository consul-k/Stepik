import random

def vibrat_sluchainii_element(l):
    return random.choice(l)

l = [1, 2, 3, 4, 5, 39, 12345]
for i in range(1000):
    print(vibrat_sluchainii_element(l))
