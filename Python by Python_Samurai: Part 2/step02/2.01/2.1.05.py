import string
alph_str = string.ascii_lowercase        

# продолжите решение здесь
d = {i:alph_str.index(i)+1 for i in alph_str}
print(d)
