from math import isqrt
class Solution:
    bulbSwitch = isqrt
    # def bulbSwitch(self, n: int) -> int:
    #     bulb = [1]*n
    #     for i in range(1, n):
    #         bulb[i::(i + 1)] = [0]*(n//(i + 1))
    #     return sum(bulb)

solution = Solution()
# print(solution.bulbSwitch(0))
# print(solution.bulbSwitch(1))
# print(solution.bulbSwitch(2))
print(solution.bulbSwitch(4))
print(solution.bulbSwitch(10))