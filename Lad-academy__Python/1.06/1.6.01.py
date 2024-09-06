a = int(input()) 
t1=-1
t2=-1
for i in range(a):
    q=int(input())
    if q>t1:
        t2=t1
        t1=q
    elif q>t2:
    	t2=q
print(t1) 
print(t2)
