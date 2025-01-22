class Solution(object):
    def wordPatternMatch(self, pattern, s):
        # patdict = dict.fromkeys((set(pattern)), None)
        # n = len(pattern)
        # m = len(s)
        # self.results = False

        # def dfs(index, start):
        #     if index == n and start == m:
        #         self.results = True
        #         return
        #     if start >= m:
        #         return
        #     for i in range(start + 1, m + 1):
        #         if patdict[pattern[index]] == None:
        #             patdict[pattern[index]] = s[start: i]
        #             dfs(index + 1, i)
        #             patdict[pattern[index]] = None
        #         else:
        #             if patdict[pattern[index]] == s[start: i]:
        #                 dfs(index + 1, i)
        #         if self.results == True:
        #             return
        # if n == 1:
        #     return True
        # dfs(0, 0)
        # return self.results == True
        def dfs(i, j):
            if i == m and j == n:
                return True
            if i == m or j == n or n - j < m - i:
                return False
            for k in range(j, n):
                t = s[j: k + 1]
                if pattern[i] in d and d[pattern[i]] == t:
                    if dfs(i + 1, k + 1):
                        return True
                elif pattern[i] not in d and t not in vis:
                    d[pattern[i]] = t
                    vis.add(t)
                    if dfs(i + 1, k + 1):
                        return True
                    d.pop(pattern[i])
                    vis.remove(t)
            return False

        m, n = len(pattern), len(s)
        d = {}
        vis = set()
        return dfs(0, 0)
  
solution = Solution()
# pattern = "d"
# s = "e"
# print(solution.wordPatternMatch(pattern, s)) # True
# pattern = "ab"
# s = "cd"
# print(solution.wordPatternMatch(pattern, s)) # True
# pattern = "ab"
# s = "aa"
# print(solution.wordPatternMatch(pattern, s)) # False
pattern = "abab"
s = "redblueredblue"
print(solution.wordPatternMatch(pattern, s)) # True

pattern = "aaaa"
s = "asdasdasdasd"
print(solution.wordPatternMatch(pattern, s)) # True

pattern = "aabb"
s = "xyzabcxzyabc"
print(solution.wordPatternMatch(pattern, s)) # False