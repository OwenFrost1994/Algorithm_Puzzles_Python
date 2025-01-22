class Solution:
    def reformat(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]
        if abs(len(letters) - len(digits)) > 1: return ""
        
        rv = []
        flag = len(letters) > len(digits)
        while letters or digits:
            rv.append(letters.pop() if flag else digits.pop())
            flag = not flag
        return rv

solution = Solution()

s = "a0b1c2"
print(solution.reformat(s))

s = "leetcode"
print(solution.reformat(s))

s = "1229857369"
print(solution.reformat(s))