a = int(input())
b = 0
c = 0
cnt = 0

while b <= a:
    c = int(input())
    b += c
    cnt += 1
print(f'Довольно!\n{b-c}\n{cnt-1}')
