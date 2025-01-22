class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num < 2:
            return num
        result = 0
        m = 1
        for i in range(9, 1, -1):
            while num % i == 0:
                num = num // i
                result = result + m * i
                m = 10*m
        if num < 2 and result <= 2**31 - 1:
            return result
        else:
            return 0

solution = Solution()
print(solution.smallestFactorization(num = 48))
print(solution.smallestFactorization(num = 15))