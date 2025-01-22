class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

solution = Solution()
n = 1
print(solution.canWinNim(n))

n = 2
print(solution.canWinNim(n))