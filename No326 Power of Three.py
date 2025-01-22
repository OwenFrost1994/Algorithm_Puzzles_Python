from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        power = log(n,3)
        x = round(power,1)
        if(pow(3,x)==n):
            return True
        else:
            return False
solution = Solution()
print(solution.isPowerOfThree(243))
print(solution.isPowerOfThree(27))
print(solution.isPowerOfThree(0))
print(solution.isPowerOfThree(-1))
