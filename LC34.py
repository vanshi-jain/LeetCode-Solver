# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       # function to do binary search for first and last position
        def findpos(first): # first is a bool flag to decide which direction to go to
            l, r = 0, len(nums)-1
            pos = -1 # default value if position is not found
            while l<=r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    pos = mid # when target is found, store this position
                    if first: # now decide the direction of array based of flag
                        r = mid - 1 # if first position means go left of array and find the first occurence
                    else:
                        l = mid + 1 # if last position then go right of the array and find last occurence

                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return pos
        
        firstpos = findpos(True)
        lastpos = findpos(False)

        return [firstpos, lastpos]
