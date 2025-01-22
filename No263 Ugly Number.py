class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n <= 6:
            return True
        
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5

        return n == 1

solution = Solution()
n = 6
print(solution.isUgly(n))
n = 1
print(solution.isUgly(n))
n = 14
print(solution.isUgly(n))