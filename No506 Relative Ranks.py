# 这里利用了python的特殊排序功能，利用另一个list的顺序排一个list

from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        index = list(range(n))
        index.sort(key = lambda x: -score[x])
        rank = ["Gold Medal","Silver Medal","Bronze Medal"]
        result = [None] * n
        for i in range(n):
            if i < 3:
                result[index[i]] = rank[i]
            else:
                result[index[i]] = str(i + 1)
        return result
    
solution = Solution()
print(solution.findRelativeRanks(score = [5,4,3,2,1]))
print(solution.findRelativeRanks(score = [10,3,8,9,4]))