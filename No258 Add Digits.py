class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            result = 0
            while num > 0:
                result = result + num % 10
                num = num //10
            num = result
        return num


solution = Solution()
num = 38
print(solution.addDigits(num))

num = 0
print(solution.addDigits(num))