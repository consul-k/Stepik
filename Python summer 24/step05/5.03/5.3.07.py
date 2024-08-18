k = 0

for i in range(int(input())):
   s = input()
   if s.count('11') >= 3:
       k += 1
print(k)
