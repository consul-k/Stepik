print("a b c d")
for a in range(0,2):
    for b in range(0,2):
        for c in range(0,2):
            for d in range(0,2):
                q=((a)<=(d))and(not((b)<=(c)))
                if q==1:
                    print(a,b,c,d)
