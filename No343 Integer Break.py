# 2 1+1 1
# 3 2+1 2
# 4 2+2 4
# 5 3+2 6
# 6 3+3 9
# 7 3+2+2 12
# 8 3+3+2 18
# 9 3+3+3 27
# 10 3+3+2+2 36
# 11 3+3+3+2 54
# 12 3+3+3+3 81
# 13 3+3+3+2+2 108
class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        if n % 3 == 1:
            return pow(3, n // 3 - 1) * 4
        if n % 3 == 2:
            return pow(3, n // 3) * 2
        return pow(3, n // 3)
solution = Solution()
print(solution.integerBreak(n = 2))
print(solution.integerBreak(n = 5))
print(solution.integerBreak(n = 8))
print(solution.integerBreak(n = 11))
print(solution.integerBreak(n = 13))