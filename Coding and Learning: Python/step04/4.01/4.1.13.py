nums = [int(x) for x in input().split()]
n = len(nums)
swapped = True

while swapped:
    swapped = False
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            swapped = True

print(*nums)
