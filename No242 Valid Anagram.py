from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = Counter(s)
        tc = Counter(t)

        if len(sc) != len(tc):
            return False
        for key in sc.keys():
            if sc[key] != tc[key]:
                return False
        return True

solution = Solution()

s = "anagram"
t = "nagaram"
print(solution.isAnagram(s, t))

s = "rat"
t = "car"
print(solution.isAnagram(s, t))