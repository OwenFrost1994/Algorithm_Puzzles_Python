import math
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        n = len(piles)
        if n == 1:
            return math.ceil(piles[0] / h)
        lv = 1
        rv = max(piles)
        while lv < rv - 1:
            mid = (lv + rv) // 2
            t = sum([math.ceil(piles[i] / mid) for i in range(n)])
            if t > h:
                    lv = mid
            else:
                    rv = mid
        t = sum([math.ceil(piles[i] / lv) for i in range(n)])
        if t <= h:
            return lv
        else:
            return rv 
    
solution = Solution()
print(solution.minEatingSpeed(piles = [2,2], h = 4))
print(solution.minEatingSpeed(piles = [2,2], h = 2))
print(solution.minEatingSpeed(piles =[312884470], h = 312884469))
print(solution.minEatingSpeed(piles = [3,6,7,11], h = 8))
print(solution.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
print(solution.minEatingSpeed(piles = [30,11,23,4,20], h = 6))
