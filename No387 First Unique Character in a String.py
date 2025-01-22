from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        n = len(s)
        for i in range(n):
            if count[s[i]] == 1:
                return i
        return -1

solution = Solution()
print(solution.firstUniqChar(s = "leetcode"))
print(solution.firstUniqChar(s = "loveleetcode"))
print(solution.firstUniqChar(s = "aabb"))