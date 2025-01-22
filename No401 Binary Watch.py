# use bin() transform int into string form binary number
from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn < 0 or turnedOn > 8:
            return []
        result = []
        for i in range(12):
            for j in range(60):
                if (bin(i) + bin(j)).count("1") == turnedOn:
                    result.append('{:d}:{:02d}'.format(i, j))
        return result

solution = Solution()
print(solution.readBinaryWatch(1))
print(solution.readBinaryWatch(2))
print(solution.readBinaryWatch(3))
print(solution.readBinaryWatch(7))
print(solution.readBinaryWatch(8))
print(solution.readBinaryWatch(9))