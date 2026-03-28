def is_correct_bracket(text):
    count = 0
    
    for char in text:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            
            if count < 0:
                return False
    
    return count == 0

txt = input()

print(is_correct_bracket(txt))
