# this problem can be transfer into a graph problem
# the equations give the connection between the nodes(variables)
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(node: str, dest:str, visited: set, answer: float, number: float):
            visited.add(node)
            if node == dest:
                answer[0] = number
                return
            for no, val in self.graph[node].items():
                if no not in visited:
                    dfs(no, dest, visited, answer, number * val)

        def buildgraph(equations: List[List[str]], values: List[float]):
            graph = {}
            for i in range(len(equations)):
                dividend, divisor = equations[i]
                if dividend not in graph:
                    graph[dividend] = {}
                if divisor not in graph:
                    graph[divisor] = {}
                graph[dividend][divisor] = values[i]
                graph[divisor][dividend] = 1.0/values[i]
            return graph
        
        self.graph = buildgraph(equations, values)
        results = []
        for dividend, divisor in queries:
            if dividend not in self.graph or divisor not in self.graph:
                results.append(-1.0)
            else:
                answer = [-1.0]
                dfs(dividend, divisor, set(), answer, 1.0)
                results.append(answer[0])
        return results
solution = Solution()
print(solution.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
print(solution.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))