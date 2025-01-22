# 他这个解法把array问题转化为net flow problem，如果存在两个及以上的点，作为流入的点，而没有相互之间的流出关系，就存在不止一个序列
# 这个是有向流问题
from collections import defaultdict, deque
from typing import List

class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        g = defaultdict(list)
        indeg = [0] * len(nums)
        for seq in sequences:
            for i  in range(len(seq) - 1):
                a = seq[i]
                b = seq[i + 1]
                g[a - 1].append(b - 1)
                indeg[b - 1] += 1
        q = deque(i for i, v in enumerate(indeg) if v == 0)
        while q:
            if len(q) > 1:
                return False
            i = q.popleft()
            for j in g[i]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)
        return True

solution = Solution()
print(solution.sequenceReconstruction(nums = [1,2,3], sequences = [[1,2],[1,3]]))
print(solution.sequenceReconstruction(nums = [1,2,3], sequences = [[1,2]]))
print(solution.sequenceReconstruction(nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]))