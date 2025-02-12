# 这个就是循环比较两个字符串str[i] str[j]，check负责检查b是不是a的子字符串

from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def check(a, b):
            i = j = 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    j += 1
                i += 1
            return j == len(b)

        n = len(strs)
        ans = -1

        for i in range(n):
            j = 0
            while j < n:
                if i == j or not check(strs[j], strs[i]):
                    j += 1
                else:
                    break
            if j == n:
                ans = max(ans, len(strs[i]))
        return ans
solution = Solution()
print(solution.findLUSlength(strs = ["aba","cdc","eae"]))
print(solution.findLUSlength(strs = ["aaa","aaa","aa"]))