deliveries = (
    ("Поставщик А", ("яблоко", "банан", "киви", "яблоко", "груша", "яблоко", "банан")),
    ("Поставщик В", ("груша", "яблоко", "банан", "яблоко", "киви", "яблоко")),
    ("Поставщик С", ("киви", "банан", "яблоко", "груша", "банан", "яблоко", "яблоко", "груша"))
)

fruit = input().strip()

total_count = 0
supplier_counts = []

for supplier, items in deliveries:
    count = 0
    for item in items:
        if item == fruit:
            count += 1
    supplier_counts.append((supplier, count))
    total_count += count

if total_count > 0:
    print(f'Общее количество товара "{fruit}" среди всех поставщиков: {total_count}')
    print("Статистика по поставщикам:")
    for supplier, count in supplier_counts:
        print(f"  {supplier}: {count} раз(а)")
else:
    print(f'Товар "{fruit}" отсутствует в доставках.')
