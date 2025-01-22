# queue[j] = [hj, kj]
# this is a dual sorting problem
# first we need highest men come out and enter the queue and in the highest men, those with smallest kj must come out
from collections import deque
from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        result = deque()
        
        for person in people:
            result.insert(person[1],person)
        return result

solution = Solution()
print(solution.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
print(solution.reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))