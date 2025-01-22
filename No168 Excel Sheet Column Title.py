class Solution:
    def convertToTitle(self, columnNumber):
        result = ""
        while columnNumber > 0:
            result = chr((columnNumber-1)%26 + 65) + result
            columnNumber = (columnNumber-1)//26
        return result

solution = Solution()

columnNumber = 1
print(solution.convertToTitle(columnNumber))

columnNumber = 28
print(solution.convertToTitle(columnNumber))

columnNumber = 701
print(solution.convertToTitle(columnNumber))