x = float(input())
result = round((x - int(x)) * 100)
print(result > 50 and result%3==0)
