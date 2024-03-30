def cylinder_volume(r, h):
    return 3.1415*h*r**2

r, h = [float(i) for i in input().split()]

print(cylinder_volume(r, h))
