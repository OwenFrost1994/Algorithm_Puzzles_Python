class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        if abs(len(s) - len(t)) > 1:
            return False
        if len(s) > len(t):
            s, t = t, s
        m = len(s)
        n = len(t)
        if m == 0 and n == 0:
            return False
        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]
        return True

solution = Solution()
print(solution.isOneEditDistance(s = "ab", t = "acb"))
print(solution.isOneEditDistance(s = "", t = ""))