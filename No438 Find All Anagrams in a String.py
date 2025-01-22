from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pc = Counter(p)
        sc = Counter()
        i, j = 0, -1
        n = len(s)
        m = len(p)
        result = []
        while j < n:
            if j - i + 1< m:
                j += 1
            elif j - i + 1 == m:
                if pc == sc:
                    result.append(i)
                j += 1
                sc[s[i]] -= 1
                if sc[s[i]] == 0:
                    sc.pop(s[i])
                i += 1                
            if j < n and s[j] not in p:
                j += 1
                i = j
                sc = Counter()
            if j < n:
                sc[s[j]] += 1
        return result

solution = Solution()
print(solution.findAnagrams(s = "cbaebabacd", p = "abc"))
print(solution.findAnagrams(s = "abab", p = "ab"))
print(solution.findAnagrams(s = "cdaebabacd", p = "abc"))