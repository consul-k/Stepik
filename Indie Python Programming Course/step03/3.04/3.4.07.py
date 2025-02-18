s, v1, v2, t1, t2 = map(int,input().split()) 
time_second = s * v2
time_first = s * v1
time_first += 2 * t1  
time_second += 2 * t2  

if time_first < time_second:
    print("First")
elif time_second < time_first:
    print("Second")
else:
    print("Friendship")
