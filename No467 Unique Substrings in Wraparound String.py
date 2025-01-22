# 很典型的dp类问题，dp也可以用dfs来求解，但是非常慢
# 这里dp的迭代其实就是看相邻的两个数字是不是连续数字是就在前一个数字的基础上加一
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        dp = [0] * 26
        k = 0
        for i, c in enumerate(s):
            if i and (ord(c) - ord(s[i - 1])) % 26 == 1:
                k += 1
            else:
                k = 1
            idx = ord(c) - ord('a')
            dp[idx] = max(dp[idx], k)
        return sum(dp)

solution = Solution()
print(solution.findSubstringInWraproundString(s = "a"))
print(solution.findSubstringInWraproundString(s = "cac"))
print(solution.findSubstringInWraproundString(s = "zab"))