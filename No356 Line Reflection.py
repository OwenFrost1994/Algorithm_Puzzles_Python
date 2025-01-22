class Solution:
    def isReflected(self, points) -> bool:
        maxx = max(points)[0]
        minx = min(points)[0]
        axis = (maxx + minx) / 2
        for point in points:
            npoint = [2*axis - point[0], point[1]]
            if npoint not in points:
                return False
        return True

solution = Solution()
print(solution.isReflected([[1,1],[-1,1]]))
print(solution.isReflected([[1,1],[-1,-1]]))