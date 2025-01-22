from typing import List
from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == inf:
            return -1
        else:
            return dp[amount]
    
solution = Solution()
print(solution.coinChange(coins = [1,2,5], amount = 11))
print(solution.coinChange(coins = [2], amount = 3))
print(solution.coinChange(coins = [1], amount = 0))