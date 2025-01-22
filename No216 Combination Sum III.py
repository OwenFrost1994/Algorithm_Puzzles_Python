class Solution:
    def combinationSum3(self, k: int, n: int):
        if n > sum(range(9 - k + 1, 10)):
            return []
        if n < sum(range(1, k + 1)):
            return []
        results = []
        self.recursion(k, n, 1, [], results)
        return results
    def recursion(self, k , n , index, result, results):
        if index == 10 or len(result) == k:
            if sum(result) == n and len(result) == k:
                results.append(result.copy())
            return
        
        for i in range(index, 10):
            result.append(i)
            if sum(result) <= n:
                self.recursion(k, n, i + 1, result, results)
            result.pop()
        
        return
solution = Solution()

k = 3
n = 7
print(solution.combinationSum3(k, n))

k = 3
n = 9
print(solution.combinationSum3(k, n))

k = 4
n = 1
print(solution.combinationSum3(k, n))