from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        results = []
        def dfs(index, path, curval, preval):
            if index == len(num):
                if curval == target:
                    results.append(path)
                return
            for j in range(index, len(num)):    
                if j > index and num[index] == "0":
                    break
                n = int(num[index:j + 1])
                if index == 0:
                    dfs(j + 1, path + num[index:j + 1], curval + n, n)
                else:
                    dfs(j + 1, path + "+" + num[index:j + 1], curval + n, n)
                    dfs(j + 1, path + "-" + num[index:j + 1], curval - n, -n)
                    dfs(j + 1, path + "*" + num[index:j + 1], curval - preval + n * preval, n * preval)
        dfs(0, "", 0, 0)
        return results
    
solution = Solution()
print(solution.addOperators(num = "123", target = 6))
print(solution.addOperators(num = "232", target = 8))
print(solution.addOperators(num = "3456237490", target = 9191))