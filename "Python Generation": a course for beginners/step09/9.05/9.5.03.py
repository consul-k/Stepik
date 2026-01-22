import re

def is_valid_number(plate):
    pattern1 = r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}_\d{2}$'
    pattern2 = r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}_\d{3}$'
    
    return bool(re.match(pattern1, plate) or re.match(pattern2, plate))

plate_number = input().strip()

if is_valid_number(plate_number):
    print("YES")
else:
    print("NO")
