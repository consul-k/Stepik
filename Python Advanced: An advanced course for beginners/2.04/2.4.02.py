temperature = int(input())

if temperature < 0:
    print("Наденьте зимнюю куртку.")
elif 0 <= temperature <= 15:
    print("Наденьте лёгкую куртку.")
else:
    print("Наденьте футболку.")
