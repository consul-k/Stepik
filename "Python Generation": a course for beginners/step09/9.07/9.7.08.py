import re

def decode_text(s):
    def replace_match(match):
        num = int(match.group(1))
        return chr(num)
    
    return re.sub(r'\[u-(\d+)\]', replace_match, s)

input_text = input()
print(decode_text(input_text))
