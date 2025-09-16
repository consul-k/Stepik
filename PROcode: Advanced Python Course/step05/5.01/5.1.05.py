n = int(input())

max_brightness = -1
brightest_color = None

for _ in range(n):
    r = int(input())
    g = int(input())
    b = int(input())
    color = (r, g, b)
    brightness = r + g + b

    if brightness > max_brightness:
        max_brightness = brightness
        brightest_color = color

print(brightest_color)
print(max_brightness)
