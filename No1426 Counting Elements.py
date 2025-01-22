from typing import List
from collections import Counter
class Solution:
    def countElements(self, arr: List[int]) -> int:
        set = Counter(arr)
        result = 0
        for key in set.keys():
            if key + 1 in set.keys():
                result += set[key]
        return result

solution = Solution()
print(solution.countElements(arr = [1,2,3]))
print(solution.countElements(arr = [1,1,3,3,5,5,7,7]))