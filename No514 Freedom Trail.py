# 这可以用dfs,每次变换字符串,但是考虑一下有可能第一次不是最短的,而是其他方向最长但是下一次最短,实际上需要cost,并且返回mincost
# 这里复现了一个高手的dp，每次深度搜索都找的是i和j之间的距离，再加深搜索j后面的key的要素，i是ring上指针现在指的位置，j是key的指针的位置
# 他反复在找最小值
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}
        def dp(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(key):
                return 0
            ans = float('inf')
            for k in range(len(ring)):
                if ring[k] == key[j]:
                    delta = abs(k - i)
                    steps = min(delta, len(ring) - delta)
                    ans = min(ans, steps + dp(k, j+1))
            memo[(i, j)] = ans
            return ans
        return dp(0, 0) + len(key)

solution = Solution()
print(solution.findRotateSteps(ring = "godding", key = "gd"))
print(solution.findRotateSteps(ing = "godding", key = "godding"))
