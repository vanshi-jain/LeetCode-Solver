# 1. Two Sum - Easy

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum(nums: list[int], target: int) -> list[int]:
    # create a dict to map target differences with indices
    res = {}
    
    for i, num in enumerate(nums):
        # 2. if num is present in res meaning you found the missing piece
        # so return the value of that key and current index as a list
        if num in res: 
            return [res[num], i] 
        # 1. insert keys as diff from target and value is index of that number
        res[target - num] = i 

# 167. Two Sum II - Input Array Is Sorted - Medium

# they just want the solution to be 1-indexed

def twoSum2(numbers: list[int], target: int) -> list[int]:
        res = {}

        for i, num in enumerate(numbers):
            if num in res:
                return [res[num], i+1]
            res[target-num] = i+1