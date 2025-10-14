def main():
    total = 0
    with open('ancient_key.txt', 'r', encoding='utf-8') as file:
        for _ in range(4):
            line = file.readline()
            total += int(line.strip())
    print(total)

if __name__ == "__main__":
    main()
