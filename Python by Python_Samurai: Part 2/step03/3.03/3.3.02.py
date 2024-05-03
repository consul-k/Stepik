st = set()

# продолжите решение здесь
a = input().split()
for word in a:
    if word.isalpha():
        st.add(word)
        
print(*sorted(st))
