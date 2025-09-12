coins = int(input())

match coins:
    case c if c > 1000:
        print("Герой может купить замок.")
    case c if 500 <= c <= 1000:
        print("Герой может купить армию.")
    case c if c < 500:
        print("Герой может купить несколько предметов или артефактов.")
