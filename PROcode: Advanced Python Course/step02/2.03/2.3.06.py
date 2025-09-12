encrypted_message = input()
n = int(input())

for _ in range(n):
    start, end = map(int, input().split())
    slice_part = encrypted_message[start:end]
    print(slice_part)
    encrypted_message = encrypted_message[:start] + encrypted_message[end:]
