from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        result = 0
        m, n = len(g), len(s)
        while i < m and j < n:
            if g[i] <= s[j]:
                result += 1
                i += 1
                j += 1
            else:
                j += 1
        return result

solution = Solution()
print(solution.findContentChildren(g = [1,2,3], s = [1,1]))
print(solution.findContentChildren(g = [1,2], s = [1,2,3]))