m='3'*100
while '333' in m or '1111' in m:
    if '333' in m:
        m=m.replace('333','1',1)
    else:
        m=m.replace('1111','3',1)
print(m)
