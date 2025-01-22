import random
from typing import List
from collections import defaultdict

class Solution:

    def __init__(self, nums: List[int]):
        self.dict = defaultdict(list)
        n = len(nums)
        for i in range(n):
            self.dict[nums[i]].append(i)

    def pick(self, target: int) -> int:
        index = random.randint(0, len(self.dict[target]) - 1)
        return self.dict[target][index]
        

solution = Solution([1, 2, 3, 3, 3])
print(solution.pick(2))
print(solution.pick(3))
print(solution.pick(1))
print(solution.pick(3))
print(solution.pick(3))