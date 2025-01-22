from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        lc = Counter(s)
        for l, c in lc.items():
            if c < k:
                return max([self.longestSubstring(sub, k) for sub in s.split(l)])
        return len(s)

solution = Solution()
print(solution.longestSubstring(s = "aaabb", k = 3))
print(solution.longestSubstring(s = "ababbc", k = 2))
print(solution.longestSubstring(s = "aabcabb", k = 2))
print(solution.longestSubstring(s = "aaabdabcb", k = 2))