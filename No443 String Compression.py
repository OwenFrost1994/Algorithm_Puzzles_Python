from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        i, k, n = 0, 0, len(chars)
        while i < n:
            j = i + 1
            while j < n and chars[j] == chars[i]:
                j += 1  
            chars[k] = chars[i]
            k += 1
            if j - i > 1:
                cnt = str(j - i)
                for c in cnt:
                    chars[k] = c
                    k += 1
            i = j
        return k

solution = Solution()
print(solution.compress(chars = ["a","a","b","b","c","c","c"]))
print(solution.compress(chars = ["a"]))
print(solution.compress(chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]))