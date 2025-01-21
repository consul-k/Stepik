import math

def calculate_buses(students):
    seats_per_bus = 24
    buses_needed = math.ceil(students / seats_per_bus)
    return buses_needed

students = int(input())
buses = calculate_buses(students)
print(buses)
