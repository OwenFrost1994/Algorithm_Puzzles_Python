from random import randint
from typing import List
class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.set = set()

    def flip(self) -> List[int]:
        x = randint(0, self.m - 1)
        y = randint(0, self.n - 1)
        while (x, y) in self.set:
            x = randint(0, self.m - 1)
            y = randint(0, self.n - 1)
        self.set.add((x, y))
        return [x, y]
        

    def reset(self) -> None:
        self.set.clear()
# 高手的代码
# class Solution:
#     def __init__(self, m: int, n: int):
#         self.m = m
#         self.n = n
#         self.total = m * n
#         self.mp = {}

#     def flip(self) -> List[int]:
#         self.total -= 1
#         x = random.randint(0, self.total)
#         idx = self.mp.get(x, x)
#         self.mp[x] = self.mp.get(self.total, self.total)
#         return [idx // self.n, idx % self.n]

#     def reset(self) -> None:
#         self.total = self.m * self.n
#         self.mp.clear()

solution = Solution(3, 1)
print(solution.flip())
print(solution.flip()) #overflow
print(solution.flip())
print(solution.reset())
print(solution.flip())