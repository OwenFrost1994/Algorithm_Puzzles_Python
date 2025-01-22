class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        def dfs(s):
            if s == 0:
                return [""]
            if s == 1:
                return ["0", "1", "8"]
            result = []
            for v in dfs(s - 2):
                for l, r in ["11", "69", "88", "96"]:
                    result.append(l + v + r)
                if s != i:
                    result.append("0" + v + "0") # if s == n, we are adding 0 in the begining of numbers. And those numbers are not ok
            return result
        
        m = len(low)
        n = len(high)
        low = int(low)
        high = int(high)
        result = 0
        for i in range(m, n + 1):
            for v in dfs(i):
                if low <= int(v) <= high:
                    result += 1
        return result
solution = Solution()
print(solution.strobogrammaticInRange("50", "100"))

print(solution.strobogrammaticInRange("0", "0"))
