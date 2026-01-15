input_str = input().strip()

import ast
data = ast.literal_eval(input_str)

cleaned_data = {}
for date, location in data.items():
    cleaned_data[date] = location.strip()

sorted_dates = sorted(cleaned_data.keys())

unique_locations = []
seen_locations = []

for date in sorted_dates:
    location = cleaned_data[date]
    if location not in seen_locations:
        seen_locations.append(location)
        unique_locations.append(location)

result = " → ".join(unique_locations)
print(f"Маршрут: {result}")
