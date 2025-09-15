import string

def find_magic_word(message: str):
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = message.split()
    for word in words:
        clean_word = word.strip(string.punctuation)
        if is_prime(len(clean_word)):
            print(clean_word)
            return
    print(None)
