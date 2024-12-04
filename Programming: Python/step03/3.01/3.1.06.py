x = int(input())
s = 0
if 500 <= x < 1000:
    s = x*0.03
elif x > 1000:
    s = x*0.05
x -= s
print(int(x))
