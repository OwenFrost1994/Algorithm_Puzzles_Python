from collections import Counter
class Solution:
    def generatePalindromes(self, s: str):
        scount = Counter(s)
        single = 0
        center = ""
        for c in scount.keys():
            if scount[c] % 2 != 0:
                if single == 0:
                    single = 1
                    center = c
                    scount[center] -= 1
                else:
                    return []
        result = []
        def dfs(center):
            if len(center) == len(s):
                result.append(center)
                return
            
            for c, n in scount.items():
                if n > 0:
                    scount[c] -= 2
                    dfs(c + center + c)
                    scount[c] += 2
        dfs(center)
        return result

solution = Solution()
print(solution.generatePalindromes(s = "aabb"))
print(solution.generatePalindromes(s = "abc"))