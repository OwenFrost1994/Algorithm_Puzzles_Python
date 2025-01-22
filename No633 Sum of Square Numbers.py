from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        while left <= right:
            num = left ** 2 + right ** 2
            if num == c:
               return True
            elif num > c:
               right -= 1
            else:
               left += 1
        return False
solution = Solution()
print(solution.judgeSquareSum(5))
print(solution.judgeSquareSum(4))
print(solution.judgeSquareSum(3))