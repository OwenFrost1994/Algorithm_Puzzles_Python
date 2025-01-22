# string has a method str.index(substr, beg).
# This method check if there is substr in str starting from beg
# So use this method. First extend str to be str + str and find where str start from position 1.
# If str has a pattern, this position is smaller than len(s)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).index(s, 1) < len(s)

solution = Solution()
print(solution.repeatedSubstringPattern("abab"))
print(solution.repeatedSubstringPattern("aba"))
print(solution.repeatedSubstringPattern("abcabcabcabc"))
