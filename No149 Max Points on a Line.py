from collections import defaultdict

class Solution:
    def maxPoints(self, points) -> int:
        N = len(points)
        D = defaultdict(set)
        if N <= 2:
            return N 
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                if y1 == y2:
                    k1, k2 = 'inf', y1
                elif x1 == x2:
                    k1, k2 = x1, 'inf'
                else:
                    k1, k2 = (x1-x2)/(y2-y1), (x2*y1-x1*y2)/(y2-y1)
                D[(k1,k2)].add(tuple(points[i]))
                D[(k1,k2)].add(tuple(points[j]))
        return max([len(i) for i in D.values()])
    
class Solution1:
    def maxPoints(self, points) -> int:
        N = len(points)
        D = defaultdict(set)
        if N <= 2:
            return N 
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                if y1 == y2:
                    k1, k2 = '0', y1
                elif x1 == x2:
                    k1, k2 = 'inf', x1
                else:
                    k1, k2 = (y2-y1)/(x2-x1), (x2*y1-x1*y2)/(x2-x1)
                D[(k1,k2)].add(tuple(points[i]))
                D[(k1,k2)].add(tuple(points[j]))
        return max([len(i) for i in D.values()])
    
solution = Solution1()

points = [[1,1],[2,2],[3,3]]
print(solution.maxPoints(points))

points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(solution.maxPoints(points))