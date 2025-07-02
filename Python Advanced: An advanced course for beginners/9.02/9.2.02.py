# Ввод ресурсов
input_data = input()

resources = set(resource.strip() for resource in input_data.split(';') if resource.strip())
unique_count = len(resources)
most_valuable = max(resources, key=len)
rarest = min(resources, key=len)

total_value = sum(len(resource) for resource in resources)

sorted_resources = sorted(resources, key=len)

print(f"\nОбщее количество уникальных ресурсов: {unique_count}")
print(f"Самый ценный ресурс: {most_valuable}")
print(f"Самый редкий ресурс: {rarest}")
print(f"Суммарная ценность ресурсов: {total_value}")
print(f"Ресурсы в отсортированном порядке: {', '.join(sorted_resources)}")
