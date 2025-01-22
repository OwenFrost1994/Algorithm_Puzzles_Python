# 这是个复合问题，排序后从小到大处理，如果一个house就在heater上那不用加radius，
# 如果不在就找最近的heater，看看需要多大的半径，那这样就更新最小的半径 radius = max(radius, distance)

from bisect import bisect_left
from math import inf

class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        mindis = 0
        for house in houses:
            if house in heaters:
                continue
            index = bisect_left(heaters, house)
            dis = inf
            if 0 < index:
                dis = min(dis, abs(house - heaters[index - 1]))
            if index < len(heaters) - 1:
                dis = min(dis, abs(house - heaters[index + 1]))
            if index < len(heaters):
                dis = min(dis, abs(house - heaters[index]))
            mindis = max(mindis, dis)
        return mindis

solution = Solution()
print(solution.findRadius([1,2,3],[2]))
print(solution.findRadius([1,2,3,4],[1,4]))
