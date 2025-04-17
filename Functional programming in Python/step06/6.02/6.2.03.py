words = input().split()

has_ought = any(word.lower().endswith("ought") for word in words)

print(has_ought)
