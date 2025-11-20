n = int(input())

instructions = tuple(int(input()) for _ in range(n))

print(f"Исходный кортеж: {instructions}")

if n == 0:
    shifted = ()
elif n == 1:
    shifted = instructions
else:
    shifted = (instructions[-1],) + instructions[:-1]

print(f"Кортеж после сдвига: {shifted}")
