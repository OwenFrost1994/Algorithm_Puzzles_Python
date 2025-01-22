class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap = sum([c.isupper() for c in word])
        return cap == 0 or cap == len(word) or (cap == 1 and word[0].isupper())

solution = Solution()
print(solution.detectCapitalUse("USA"))
print(solution.detectCapitalUse("FlaG"))
print(solution.detectCapitalUse("leetcode"))
print(solution.detectCapitalUse("Google"))