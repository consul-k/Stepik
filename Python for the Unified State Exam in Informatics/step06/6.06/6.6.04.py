count = 0
for a1 in 'ДИОНС':
    for a2 in 'ДИОНС':
        for a3 in 'ДИОНС':
            for a4 in 'ДИОНС':
                for a5 in 'ДИОНС':
                    s = a1 + a2 + a3 + a4 + a5
                    if (s.count('Д') + s.count('Н') + s.count('С')) <= (s.count('И') + s.count('О')):
                        count += 1
print(count)
