s = input()
def fix_start(s):
    first_letter = s[0]
    return s[0]+s[1:].replace(first_letter, '*')
            

print(fix_start(s))
