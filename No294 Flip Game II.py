class Solution:
    def canWin(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if s[i:i + 2] == "++":
                if not self.canWin(s[:i] + "--" + s[i + 2:]):
                    return True
        return False

solution = Solution()
print(solution.canWin("++++"))
print(solution.canWin("+"))