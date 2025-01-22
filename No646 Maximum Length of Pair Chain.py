from math import inf
from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        ans, cur = 0, -inf
        for a, b in sorted(pairs, key=lambda x: x[1]):
            if cur < a:
                cur = b
                ans += 1
        return ans
    
solution = Solution()
print(solution.findLongestChain(pairs = [[1,2],[2,3],[3,4]]))
print(solution.findLongestChain(pairs = [[1,2],[7,8],[4,5]]))