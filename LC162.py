# A peak element is an element that is strictly greater than its neighbors.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        l, r = 0,  len(nums)-1
        
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[mid+1]: # no target given, so assume next element as target and compare the values 
                r = mid
            else:
                l = mid + 1
        return l
