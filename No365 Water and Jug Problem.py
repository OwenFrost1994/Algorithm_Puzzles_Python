from math import gcd
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        if jug2Capacity == 0 or jug2Capacity == 0:
            if targetCapacity == 0:
                return True
            elif jug2Capacity + jug2Capacity == targetCapacity:
                return True
            else:
                return False
        return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0

solution = Solution()
print(solution.canMeasureWater(jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4))
print(solution.canMeasureWater(jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5))
print(solution.canMeasureWater(jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3))