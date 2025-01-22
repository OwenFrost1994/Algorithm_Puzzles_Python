from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        lc = defaultdict(int) # or, cnt = defau
        i, result = 0, 0
        for j, c in enumerate(s):
            lc[c] += 1
            while len(lc) > k:
                lc[s[i]] -= 1
                if lc[s[i]] == 0:
                    lc.pop(s[i])
                i += 1
            result = max(result, j - i + 1)
        return result

solution = Solution()
print(solution.lengthOfLongestSubstringKDistinct(s = "eceba", k = 2))
print(solution.lengthOfLongestSubstringKDistinct(s = "aa", k = 1))