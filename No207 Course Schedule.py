class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        indegree = [0] * numCourses
        adj = [[] for x in range(numCourses)]

        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        visited = 0
        while queue:
            node = queue.pop(0)
            visited += 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return visited == numCourses

solution = Solution()

numCourses = 6
prerequisites = [[1,0], [1,2], [2,3], [2,4], [2,5], [3,1], [4,5]]
print(solution.canFinish(numCourses, prerequisites))

numCourses = 2
prerequisites = [[1,0]]
print(solution.canFinish(numCourses, prerequisites))

numCourses = 2
prerequisites = [[1,0],[0,1]]
print(solution.canFinish(numCourses, prerequisites))