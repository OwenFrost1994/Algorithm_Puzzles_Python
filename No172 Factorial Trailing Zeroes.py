class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)

class Solution1:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        if n >= 5:
            result += n / 5
        if n >= 25:
            result += n / 25
        if n >= 125:
            result += n / 125
        if n >= 625:
            result += n / 625
        if n >= 3125:
            result += n / 3125
        return result

solution = Solution()
n = 3
print(solution.trailingZeroes(n))
n = 5
print(solution.trailingZeroes(n))
n = 0
print(solution.trailingZeroes(n))