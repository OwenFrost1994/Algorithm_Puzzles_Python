from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lc = Counter()
        i = 0
        j = 0
        n = len(s)
        result = 0
        maxcnt = 0
        while i < n:
            lc[s[i]] += 1
            maxcnt = max(maxcnt, lc[s[i]])
            if i - j + 1 > maxcnt + k: # contains more letters than the repeated maxcnt letter and k extra letter
                lc[s[j]] -= 1
                j += 1
            else:
                result = max(result, i - j + 1)
            i += 1
        return result

solution = Solution()
print(solution.characterReplacement(s = "ABAB", k = 2))
print(solution.characterReplacement(s = "AABABBA", k = 1))