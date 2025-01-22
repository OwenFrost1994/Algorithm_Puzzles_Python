from math import log, floor
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        power = log(n,2)
        if power % 2 == 0:
            return True
        else:
            return False
solution = Solution()
print(solution.isPowerOfFour(536870912))
print(solution.isPowerOfFour(16))
print(solution.isPowerOfFour(5))
print(solution.isPowerOfFour(1))
print(solution.isPowerOfFour(2))
print(solution.isPowerOfFour(8))