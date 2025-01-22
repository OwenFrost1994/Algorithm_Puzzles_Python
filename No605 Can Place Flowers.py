from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if sum(flowerbed[i - 1 : i + 2]) == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0

solution = Solution()
print(solution.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
print(solution.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))
print(solution.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))