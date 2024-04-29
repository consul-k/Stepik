crypto = {
    'Биткоин': 38.623,
    'Эфириум': 2092.98,
    'USDt': 1.0002,
    'BNB': 228.60,
    'XRP': 0.60898,
    'Solana': 60.995,
    'USD Coin': 0.9995,
    'Cardano': 0.3813,
    'Dogecoin': 0.083747,
    }

# продолжите решение здесь
c = input()
if c not in crypto:
    print(f'Нет данных по {c}')
else:
    print(crypto[c])
