from fnmatch import fnmatch

for n in range(21025,10**10+1,21025):
    s=str(n)
    p='12*34?5'
    if fnmatch(s,p):
        if s.count('0')+s.count('2')+s.count('4')+s.count('6')+s.count('8')==s.count('1')+s.count('3')+s.count('5')+s.count('7')+s.count('9'):
            print(n,n//21025)
