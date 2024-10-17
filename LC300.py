class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # cache memory to store length of subsequence for each index
        # set default value to 1 for each index
        LIS = [1] * len(nums)
        
        # start outer loop from reverse list 
        # and inner loop from forward list starting from current index
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                # check if curr num is less than next --> increasing order
                if nums[i] < nums[j]:
                    # if true then find max subsequence len for this curr index and jth
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)

