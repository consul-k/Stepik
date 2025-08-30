print("x y z w")
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                a=not(x)
                s=not(y)
                d=not(z)
                f=not(w)
                q=((z)<=(w))*(y)*(a)
                if q==1:
                    print(x,y,z,w)
