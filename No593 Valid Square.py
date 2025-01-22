# any three points in a square could form a triangle
from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def check(a, b, c):
            d1 = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
            d2 = (b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2
            d3 = (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2
            return d1 > 0 and d2 > 0 and d3 > 0 and ((d1 == d2 and d1 + d2 == d3) or  (d2 == d3 and d2 + d3 == d1) or (d1 == d3 and d1 + d3 == d2))
        
        return check(p1, p2, p3) and check(p2, p3, p4) and check(p1, p3, p4) and check(p1, p2, p4)

solution = Solution()
print(solution.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))
print(solution.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]))
print(solution.validSquare(p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]))