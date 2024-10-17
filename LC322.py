class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # this approach is dfs with dp for sub-problems
        # let's make a list of size amount+1 as we are starting from 0
        # to calculate the dp[amount], we are doing bottom-up approach
        # which starts from dp[0] the end of the coins change from total amount
        # imagine a tree starting from amount and goes all the way down to 0 with branches as coin types
        total = amount + 1
        dp = [total] * (total)
        dp[0] = 0

        for a in range(1, total):
            for c in coins:
                if a - c >= 0: # non-negative change
                    # recurrence equation for current amount and change amount
                    dp[a] = min(dp[a], 1 + dp[a - c])
            
        return dp[amount] if dp[amount] != total else -1
