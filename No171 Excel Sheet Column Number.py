class Solution:
    def titleToNumber(self, columnTitle):
        result = 0
        for s in columnTitle:
            result = result*26 + (ord(s) -64)
        return result

solution = Solution()

columnTitle = "A"
print(solution.titleToNumber(columnTitle))

columnTitle = "AB"
print(solution.titleToNumber(columnTitle))

columnTitle = "ZY"
print(solution.titleToNumber(columnTitle))