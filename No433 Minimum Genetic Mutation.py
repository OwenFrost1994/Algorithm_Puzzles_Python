# BFS search 搜索只有一个字母不一样的下级节点
from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return False
        depth = 0
        q = deque([startGene])
        visited = set()
        while q:
            depth += 1
            n = len(q)
            for i in range(n):
                gene = q.popleft()
                for b in bank:
                    if b not in visited and sum([gene[i] != b[i] for i in range(8)]) == 1:
                        if b == endGene:
                            return depth
                        else:
                            q.append(b)
                            visited.add(b)
        return -1

solution = Solution()
print(solution.minMutation(startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]))
print(solution.minMutation(startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))
