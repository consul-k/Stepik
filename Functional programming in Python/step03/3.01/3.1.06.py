def is_leap(n):
    if (n%4==0 and n%100!=0) or n%400==0:
        return True
    else:
        return False
    
def get_leap_years(y1, y2):
    cnt = []
    for i in range(y1, y2):
        if is_leap(i):
            cnt.append(i)
    return sorted(cnt)
