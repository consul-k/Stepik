count=0
for a1 in 'ШКОЛА':
    for a2 in 'ШКОЛА':
        for a3 in 'ШКОЛА':
            for a4 in 'ШКОЛА':
                for a5 in 'ШКОЛА':
                    for a6 in 'ШКОЛА':
                        slovo=a1+a2+a3+a4+a5+a6
                        if ("АО" not in slovo) and ("ОА" not in slovo) and ("ОО" not in slovo) and "АА" not in slovo:
                            count+=1

print(count)
