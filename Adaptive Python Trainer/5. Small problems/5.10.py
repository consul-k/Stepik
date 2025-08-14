to_meters = {
    "mile": 1609,
    "yard": 0.9144,
    "foot": 0.3048,
    "inch": 0.0254,
    "km": 1000,
    "m": 1,
    "cm": 0.01,
    "mm": 0.001
}

value_str, unit_from, _, unit_to = input().split()
value = float(value_str)

meters = value * to_meters[unit_from]

result = meters / to_meters[unit_to]

print(f"{result:.2e}")
