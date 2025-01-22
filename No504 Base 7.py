class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        result = ""
        sign = ""
        if num < 0:
            sign = "-"
            num = abs(num)
        while num > 0:
            result = str(num % 7) + result
            num = num // 7
        return sign + result
    
solution = Solution()
print(solution.convertToBase7(100))
print(solution.convertToBase7(-7))
