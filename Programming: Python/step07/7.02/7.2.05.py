def count_divisors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

def main():
    n = int(input())
    for i in range(1, n + 1):
        divisors_count = count_divisors(i)
        print(f"{i}{'+' * divisors_count}")

if __name__ == "__main__":
    main()
