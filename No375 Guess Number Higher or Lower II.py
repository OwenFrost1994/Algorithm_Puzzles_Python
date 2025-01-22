# dp[i][j] is the needed amount of money we guess from i to j
# traverse each interval [j, i], maintain a global minimum global_min variable
# then traverse every number in the interval to calculate the local maximum local_max = k + max(dp[j][k-1] , dp[k + 1][i])
# this happens to divide the interval into two sections at each position,
# and then take the cost of the current position plus the larger cost of the two left and right sections as the local maximum value.
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        if n == 1:
            return 0
        starting_index = 1 if n % 2 == 0 else 2
        selected_nums = [i for i in range(starting_index, n, 2)]
        selected_nums_length = len(selected_nums)
        dp = [[0] * selected_nums_length for _ in range(selected_nums_length)]

        for i in range(selected_nums_length):
            dp[i][i] = selected_nums[i]

        for length in range(2, selected_nums_length + 1):
            for i in range(selected_nums_length - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")
                for k in range(i, j + 1):
                    dp_left = dp[i][k - 1] if k != 0 else 0
                    dp_right = dp[k + 1][j] if k != j else 0
                    dp[i][j] = min(dp[i][j], selected_nums[k] + max(dp_left, dp_right))

        return dp[0][-1]
    
solution = Solution()
print(solution.getMoneyAmount(2))
print(solution.getMoneyAmount(10))
print(solution.getMoneyAmount(20))