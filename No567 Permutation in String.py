from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1c = Counter(s1)
        s2c = Counter()
        i, j = 0, -1
        n = len(s1)
        m = len(s2)
        while j < m:
            if j - i + 1 < n:
                j += 1
            elif j - i + 1 == n:
                if s1c == s2c:
                    return True
                j += 1
                s2c[s2[i]] -= 1
                if s2c[s2[i]] == 0:
                    s2c.pop(s2[i])
                i += 1                
            while j < m and s2[j] not in s1:
                j += 1
                i = j
                s2c = Counter()
            if j < m:
                s2c[s2[j]] += 1
        return False
    
solution = Solution()
print(solution.checkInclusion(s1 = "ab", s2 = "eidbaooo"))
print(solution.checkInclusion(s1 = "ab", s2 = "eidboaoo"))
print(solution.checkInclusion(s1 = "abo", s2 = "eidboaoo"))