def find_minimum(nums):
    res = nums[0] if nums else None
    for num in nums[1:]:
        if num < res:
            res = num
    return res

print(find_minimum([9, -6, 0, -3, 3]))
