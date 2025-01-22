from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = Counter(ransomNote)
        mag = Counter(magazine)
        for key in ran.keys():
            if key in mag.keys():
                if ran[key] > mag[key]:
                    return False
            else:
                return False
        return True
    
solution = Solution()
print(solution.canConstruct(ransomNote = "a", magazine = "b"))
print(solution.canConstruct(ransomNote = "aa", magazine = "ab"))
print(solution.canConstruct(ransomNote = "aa", magazine = "aab"))