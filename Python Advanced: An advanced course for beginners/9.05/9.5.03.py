def is_subsequence(sub, full):
    it = iter(full)
    return all(char in it for char in sub)

def main():
    scroll1 = input().strip()
    scroll2 = input().strip()

    set1 = set(scroll1.replace(' ', ''))
    set2 = set(scroll2.replace(' ', ''))

    if is_subsequence(scroll1, scroll2):
        print("Первый свиток скрыт в тексте второго.")
    elif is_subsequence(scroll2, scroll1):
        print("Второй свиток скрыт в тексте первого.")
    elif set1 & set2:
        print("Свитки имеют общие символы, но их порядок различен.")
    else:
        print("Свитки принадлежат разным эпохам.")

if __name__ == "__main__":
    main()
