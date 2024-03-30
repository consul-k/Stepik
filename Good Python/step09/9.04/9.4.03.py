def cylinder_surface_area(r,h):
    return 2 * 3.1415 * r * (r + h)

r, h = [float(i) for i in input().split()]

print(cylinder_surface_area(r,h))
