s = input()
    
b = s.find('h') 
e = s.rfind('h')
    
print(s[:b] + s[e + (e != -1):])
