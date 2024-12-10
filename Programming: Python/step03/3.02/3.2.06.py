nums = [int(input()) for _ in range(3)] 
if any(i % 2 == 0 for i in nums) and any(i % 2 != 0 for i in nums): 
    print("YES") 
else: 
    print("NO")
