from collections import defaultdict
from typing import List

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        n = len(picture[0])
        row = defaultdict(list)
        col = defaultdict(list)
        result = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    row[i].append(j)
                    col[j].append(i)
        for i in range(m):
            if len(row[i]) == 1 and len(col[row[i][0]]) == 1:
                result += 1
        return result

solution = Solution()
print(solution.findLonelyPixel([["W","W","B"],["W","B","W"],["B","W","W"]]))
print(solution.findLonelyPixel(picture = [["B","B","B"],["B","B","W"],["B","B","B"]]))