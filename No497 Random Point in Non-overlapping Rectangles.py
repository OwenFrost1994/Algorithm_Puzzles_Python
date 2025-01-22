from bisect import bisect_left
from random import randint
from typing import List
import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.n = len(rects)

    def pick(self) -> List[int]:
        index = randint(0, self.n - 1)
        return [randint(self.rects[index][0], self.rects[index][2]), randint(self.rects[index][1], self.rects[index][3])]
# 非常的诡异，高手做的这个能过我的过不了
class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.s = [0] * len(rects)
        for i, (x1, y1, x2, y2) in enumerate(rects):
            self.s[i] = self.s[i - 1] + (x2 - x1 + 1) * (y2 - y1 + 1)

    def pick(self) -> List[int]:
        v = random.randint(1, self.s[-1])
        idx = bisect_left(self.s, v)
        x1, y1, x2, y2 = self.rects[idx]
        return [random.randint(x1, x2), random.randint(y1, y2)]

solution = Solution([[-2, -2, 1, 1], [2, 2, 4, 6]])
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())

solution = Solution([[1,1,5,5]])
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())

solution = Solution([[-2,-2,-1,-1],[1,0,3,0]])
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())