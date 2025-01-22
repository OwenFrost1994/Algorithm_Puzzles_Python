import re
class Solution:
    def countSegments(self, s: str) -> int:
        s = s.split(" ")
        result = []
        for l in s:
            if l != "":
                result.append(l)
        return len(result)
    
solution = Solution()
print(solution.countSegments(s = "                "))
print(solution.countSegments(s = "Hello, my name is John"))
print(solution.countSegments(s = "Hello"))