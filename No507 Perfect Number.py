from math import sqrt

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        n = int(sqrt(num))
        divisor = [1]
        for i in range(2, n + 1):
            if num % i == 0:
                if num // i == i:
                    divisor.append(i)
                else:
                    divisor.append(i)
                    divisor.append(num // i)
        return sum(divisor) == num

solution = Solution()
print(solution.checkPerfectNumber(1))
print(solution.checkPerfectNumber(28))
print(solution.checkPerfectNumber(7))