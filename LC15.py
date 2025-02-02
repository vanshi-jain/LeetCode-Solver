# 3 sum - break it down to 2 sum and set that as target for the negative of first value
# O(n^2) time complexity
# sort to avoid hitting duplicate values
from typing import List

def threeSum(nums: List(int)):
    nums = sorted(nums)
    result = []

    for i in range(len(nums)):
        # avoid hitting same i value
        if i > 0 and nums[i] == nums[i-1]:
            continue

        x, target = nums[i], -nums[i]
        l, r = i+1, len(nums)-1 # two pointers- left and right
        while l < r:
            if nums[l] + nums[r] == target:
                result.append([x, nums[l], nums[r]])
                # avoid hitting same l and r values
                while l < r and nums[l] == nums[l+1]:
                    l += 1 
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                # increment l and decrement r
                l += 1
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    return result
