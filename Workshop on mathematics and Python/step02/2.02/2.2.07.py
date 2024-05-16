import math

def dodecahedron_properties(edge_length):
    # Вычисление площади поверхности
    surface_area = 3 * math.sqrt(25 + 10 * math.sqrt(5)) * (edge_length ** 2)
    # Вычисление объёма
    volume = (15 + 7 * math.sqrt(5)) / 4 * (edge_length ** 3)
    return round(surface_area, 2), round(volume, 2)

# Пример использования
edge_length = float(input())
surface_area, volume = dodecahedron_properties(edge_length)
print(surface_area)
print(volume)
