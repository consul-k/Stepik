positions = {}

for employee in employees:
    position = employee["position"]

    if position in positions:
        positions[position] += 1
    else:
        positions[position] = 1
