from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        scount = Counter(s)
        single = 0
        for c in scount.keys():
            if scount[c] % 2 != 0:
                if single == 0:
                    single = 1
                else:
                    return False
        return True
    
solution = Solution()
print(solution.canPermutePalindrome(s = "code"))
print(solution.canPermutePalindrome(s = "aab"))
print(solution.canPermutePalindrome(s = "carerac"))