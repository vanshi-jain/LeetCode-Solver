# /find-minimum-in-rotated-sorted-array
# dont get confused by rotated array, the only thing to figure out is which side of the array to search into
# and to get that, we check if middle value is greater than right value of the array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            return nums[0]
     
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1 # greater middle value means check right array as you need the min val
            else:
                r = mid # else turn to left side of the array
        return nums[l]
