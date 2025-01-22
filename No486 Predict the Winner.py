from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def dfs(l, r):
            if l == r:
                return nums[l]
            left = nums[l] - dfs(l + 1, r) # choose the most left, and the the next player select, to see the score difference between two player
            right = nums[r] - dfs(l, r - 1) # choose the most right, and the the next player select
            return max(left,  right)

        return dfs(0, len(nums) - 1) >= 0

# dp法比较抽象, 有一个反推过程，从长度为1的nums往回加
class Solution1:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0]*n for _ in range(n + 1)]
        for i in range(n):
            dp[1][i] = nums[i]
        for i in range(2, n + 1):
            for j in range(0, n - i + 1):
                dp[i][j] = max(nums[j] - dp[i - 1][j + 1], nums[j + i - 1] - dp[i - 1][j])
                # 这里nums[j]和nums[j + i - 1]分别是一个array的两端，分别减去了前一行玩家的选择的差最大化看是不是负值
                # nums[j]要减去前一个玩家(i-1)选择另一个值(j+1)，nums[j + i - 1] 减去前一个玩家选择的另一个值(j)来找最大
        return dp[n][0] >= 0
    
# solution = Solution()
# print(solution.PredictTheWinner(nums = [1,5,2]))
# print(solution.PredictTheWinner(nums = [1,5,233,7]))
solution = Solution1()
print(solution.PredictTheWinner(nums = [1,5,2]))
print(solution.PredictTheWinner(nums = [1,5,233,7]))