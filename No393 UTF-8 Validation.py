from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = 0
        for num in data:
            if n > 0:
                if num >> 6 != 0b10:
                    return False
                n -= 1
            elif num >> 7 == 0b0:
                n = 0
            elif num >> 5 == 0b110:
                n = 1
            elif num >> 4 == 0b1110:
                n = 2
            elif num >> 3 == 0b11110:
                n = 3
            else:
                return False
        return n == 0
    
solution = Solution()
print(bin(255))
print(solution.validUtf8([255]))
print(bin(237))
print(solution.validUtf8([237]))
print(solution.validUtf8([197,130,1]))
print(solution.validUtf8([235,140,4]))