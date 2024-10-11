class Solution:
    def climbStairs(self, n: int) -> int:
        # brute force approach - imagine a decision tree with root 0 and two paths +1 and +2
        # this involves repeated tasks - sub-problems
        # bottom-up dp approach - conisder starting from n and moving back up to step 0
        # count all the ways possible to reach there
        # just like fibonacci series

        count_one, count_two = 1, 1

        for i in range(n-1):
            temp = count_one
            count_one += count_two
            count_two = temp

        return count_one
