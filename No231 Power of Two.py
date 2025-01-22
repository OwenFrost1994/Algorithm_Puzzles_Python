class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while(n > 0):
            if n % 2 == 0:
                n = n//2
                continue
            else:
                return False
        if n == 0:
            return True
        else:
            return False


solution = Solution()

n = 1
print(solution.isPowerOfTwo(n))

n = 16
print(solution.isPowerOfTwo(n))

n = 3
print(solution.isPowerOfTwo(n))