n = input()
i = 0
cnt = 0

while i < len(n):
    if int(n[i])%2==0:
        cnt+=1
    i+=1
print(cnt)
