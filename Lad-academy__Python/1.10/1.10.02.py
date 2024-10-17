def compress_list(nums):
    non_zero_index = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1

    for i in range(non_zero_index, len(nums)):
        nums[i] = 0

    return nums

nums = list(map(int, input().split()))

result = compress_list(nums)

print(" ".join(map(str, result)))
