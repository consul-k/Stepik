c=0
for a1 in '1234567':
    for a2 in '01234567':
        for a3 in '01234567':
            for a4 in '01234567':
                w=a1+a2+a3+a4
                if len(set(w))==4:
                    if '26' not in w and '62' not in w:
                        c+=1
print(c)  
