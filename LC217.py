# 217. Contains Duplicate - Easy

# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

def containsDuplicate(nums: list[int]) -> bool:
    # use set data type as it inherently doesn't take duplicates unlike lists
    nodupes = set()

    for num in nums:
        if num in nodupes:
            return True
        nodupes.add(num)
    
    return False