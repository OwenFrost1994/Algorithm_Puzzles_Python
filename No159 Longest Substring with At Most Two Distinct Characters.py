class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        maxlen = 1
        ccount = {}
        n = len(s)
        i = 0
        for j in range(n):
            if s[j] not in ccount.keys():
                ccount[s[j]] = 1
            else:
                ccount[s[j]] += 1
            if len(ccount) > 2:
                ccount[s[i]] -= 1
                if ccount[s[i]] == 0:
                    ccount.pop(s[i])
                i += 1
            maxlen = max(maxlen, j - i + 1)
        return maxlen

solution = Solution()
print(solution.lengthOfLongestSubstringTwoDistinct("ecebbba"))
print(solution.lengthOfLongestSubstringTwoDistinct("ccaabbb"))