from itertools import accumulate
from random import randint
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.weight = list(accumulate(w))

    def pickIndex(self) -> int:
        val = randint(1, self.weight[-1])
        l, r = 0, len(self.weight) - 1
        while l < r:
            mid = (l + r) // 2
            if self.weight[mid] >= val:
                r = mid
            else:
                l = mid + 1
        return l

solution = Solution([1])
print(solution.pickIndex())
print(solution.pickIndex())
solution = Solution([1,3])
print(solution.pickIndex())
print(solution.pickIndex())