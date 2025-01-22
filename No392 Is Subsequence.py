class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j, m, n = 0, 0, len(s), len(t)
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == m:
            return True
        if j == n:
            return False

solution = Solution()
print(solution.isSubsequence(s = "abc", t = "ahbgdc"))
print(solution.isSubsequence(s = "axc", t = "ahbgdc"))