from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        if map1 == map2:
            return True
        return False

class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        N = len(s)
        D = defaultdict(set)

        for i in range(N):
            D[s[i]].add(t[i])

        for key in D.keys():
            if len(D[key]) > 1:
                return False
        
        E = defaultdict(set)
        for i in range(N):
            E[t[i]].add(s[i])
        for key in E.keys():
            if len(E[key]) > 1:
                return False
        return True

solution = Solution1()
s = "badc"
t = "baba"
print(solution.isIsomorphic(s,t))

s = "egg"
t = "add"
print(solution.isIsomorphic(s,t))

s = "foo"
t = "bar"
print(solution.isIsomorphic(s,t))

s = "paper"
t = "title"
print(solution.isIsomorphic(s,t))