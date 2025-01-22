from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Ra = deque()
        Dir = deque()
        n = len(senate)
        for i in range(len(senate)):
            if senate[i] == "R":
                Ra.append(i)
            else:
                Dir.append(i)
        while len(Ra) != 0 and len(Dir) != 0:
            if Ra[0] < Dir[0]:
                Ra.append(n)
            else:
                Dir.append(n)
            n += 1
            Ra.popleft()
            Dir.popleft()
        if len(Ra) > 0:
            return "Radiant"
        return "Dire"
    
solution = Solution()
print(solution.predictPartyVictory(senate = "RD"))
print(solution.predictPartyVictory(senate = "RDD"))