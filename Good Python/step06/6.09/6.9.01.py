def check_plagiarism(s, t):
    s = s.strip().lower()
    t = t.strip().lower()
    return s == t
s = input()
t = input()
print(check_plagiarism(s, t))
