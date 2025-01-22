from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs = Counter(s)
        ct = Counter(t)
        for key in ct.keys():
            if not key in cs:
                return key
            if ct[key] > cs[key]:
                return key

solution = Solution()
print(solution.findTheDifference(s = "abcd", t = "abcde"))
print(solution.findTheDifference(s = "", t = "y"))