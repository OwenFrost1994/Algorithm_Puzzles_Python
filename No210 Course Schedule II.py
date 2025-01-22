class Solution:
    def findOrder(self, numCourses: int, prerequisites):
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
        course = []
        while queue:
            node = queue.pop(0)
            course.append(node)
            visited += 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if visited == numCourses:
            return course
        else:
            return []
    
solution = Solution()
numCourses = 6
prerequisites = [[1,0], [1,2], [2,3], [2,4], [2,5], [3,1], [4,5]]
print(solution.findOrder(numCourses, prerequisites))

numCourses = 2
prerequisites = [[1,0]]
print(solution.findOrder(numCourses, prerequisites))

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(solution.findOrder(numCourses, prerequisites))

numCourses = 1
prerequisites = []
print(solution.findOrder(numCourses, prerequisites))