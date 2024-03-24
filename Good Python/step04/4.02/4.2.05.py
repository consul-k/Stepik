v = float(input())
t = int(input())
x = float(input())
if x/v*60<=t:
    print('Сакура придет вовремя')
else:
    print((x/v*60)-t)
