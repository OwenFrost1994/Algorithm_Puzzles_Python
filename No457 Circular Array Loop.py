# 这一个graph找环的问题
from collections import defaultdict, deque
from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        g = defaultdict(list)
        indeg = [0] * len(nums)
        n = len(nums)
        for i in range(n):
            g[i].append((i + nums[i]) % n)
            indeg[(i + nums[i]) % n] += 1
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for j in g[node]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)
        isloop = 0
        visited = []
        for i in range(n):
            if indeg[i] > 0 and i not in visited:
                visited.append(i)
                loop = [i]
                if nums[i] > 0:
                    direct = 1
                else:
                    direct = 0
                next = (i + nums[i]) % n
                while next < 0:
                    next += n 
                while next not in visited:
                    visited.append(next)
                    loop.append(next)
                    if (nums[next] > 0 and direct == 0) or (nums[next] < 0 and direct == 1):
                        break
                    next = (next + nums[next]) % n
                    while next < 0:
                        next += n
                if next == i and len(loop) > 1:
                    isloop = 1
                        
        return isloop == 1

solution = Solution()
print(solution.circularArrayLoop(nums = [-2,1,-1,-2,-2]))
print(solution.circularArrayLoop(nums = [2,-1,1,2,2]))
print(solution.circularArrayLoop(nums = [-1,-2,-3,-4,-5,6]))
print(solution.circularArrayLoop(nums = [1,-1,5,1,4]))