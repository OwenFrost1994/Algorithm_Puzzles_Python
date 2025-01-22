class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        result = 0
        inter = 9
        for i in range(1, n + 1):
            if i == 1:
                result += 10
            else:
                inter = inter * (10 - i + 1)
                result += inter
        return result

solution = Solution()
print(solution.countNumbersWithUniqueDigits(0))
print(solution.countNumbersWithUniqueDigits(1))
print(solution.countNumbersWithUniqueDigits(2))
print(solution.countNumbersWithUniqueDigits(3))