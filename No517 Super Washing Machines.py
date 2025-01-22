# 一次一动只能移动一件衣服，只能给临近的洗衣机移动但是可以在多个洗衣机
# 1     0 <-- 5    =>    1     1     4
# 1 <-- 1 <-- 4    =>    2     1     3
# 2     1 <-- 3    =>    2     2     2
# 这里其实就需要看到移动的次数最多的就是左侧一群洗衣机和右侧一群洗衣机间的差最大的时候就是最多的移动次数
# 另外考虑的就是diff最大的情况，这时候最大diff是决定一动次数最多的时候
# https://leetcode.com/problems/super-washing-machines/solutions/3367563/python-3-4-lines-w-map-accumulate-t-m-99-6/
from typing import List

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        if sum(machines) % len(machines) != 0:
            return -1
        t = sum(machines) // len(machines)
        diffsum = 0
        maxdiff = 0
        maxsum = 0
        for num in machines:
            diff = num - t
            maxdiff = max(maxdiff, diff)
            diffsum += diff
            maxsum = max(maxsum, abs(diffsum))
        return max(maxdiff, maxsum)
    
solution = Solution()
print(solution.findMinMoves(machines = [1,0,5]))
print(solution.findMinMoves(machines = [0,3,0]))
print(solution.findMinMoves(machines = [0,2,0]))