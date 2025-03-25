# search-in-rotated-sorted-array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        # this is usual binary search except one extra layer which checks either side of the array is sorted
        while l<=r :
            mid = (l+r) // 2
            num = nums[mid]
            if num == target:
                return mid
            # to check lower value than target, first make sure left array is sorted
            if nums[l] <= num: # left array is sorted
                if nums[l] <= target < num:
                    r = mid - 1 # then search in left array
                else:
                    l = mid + 1 # else search in right array
            else: # right half is sorted
                if num < target <= nums[r]: # means target lies in outer right array
                    l = mid + 1 # so search in right side
                else:
                    r = mid - 1
        return -1
            
