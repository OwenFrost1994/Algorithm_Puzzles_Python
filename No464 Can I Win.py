# 这是一个dfs问题，但是在这里玩了一个花活，用一个int的不同位来存储是不是占用了
# 但是要注意一个问题，就是在达到target的时候回true（win），或者第二个玩家不能赢的情况下也回true
# 在dfs里面除了传递数的占用情况还得传递以及加了多少
# 一开始如果所有的数加起来都没有target大那就直接回false

from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @lru_cache
        def dfs(nums, t):
            for i in range(1, maxChoosableInteger + 1):
                if nums & 1 << i == 0:
                    if t + i >= desiredTotal or not dfs(nums | 1 << i, t + i):
                        return True
            return False
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        return dfs(0, 0)

class Solution1:
    def canIWin(self, maxInt: int, total: int) -> bool:
        if maxInt * (maxInt+1) / 2 < total: return False

        # @cache
        def func(nums, total):
            #condition2
            if any(total <= x for x in nums): return True 
            #condition3
            return any(not func(nums-{x}, total-x) for x in nums)

        return func(frozenset(range(1,maxInt+1)), total)
class Solution2:
    def canIWin(self, maxInt: int, total: int) -> bool:
        # @functools.lru_cache(None)s
        def dp(nums, left):
            return any(left - n <= 0 or not dp(frozenset(nums - {n}), left - n) for n in nums)
        
        return  (1 + maxInt) * maxInt // 2 >= total and dp(frozenset(range(1, maxInt + 1)), total)
solution = Solution1()
print(solution.canIWin(maxChoosableInteger = 10, desiredTotal = 11))
print(solution.canIWin(maxChoosableInteger = 10, desiredTotal = 0))
print(solution.canIWin(maxChoosableInteger = 10, desiredTotal = 1))