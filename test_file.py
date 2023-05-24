def find_minimum(nums):
    if not nums:
        return None
    res = nums[0]
    for num in nums[1:]:
        if num < res:
            res = num
    return res

print(find_minimum([9, -6, 0, -3, 3]))
