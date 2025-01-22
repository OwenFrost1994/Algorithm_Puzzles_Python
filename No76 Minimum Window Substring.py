import copy
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tlist = [*t]
        smap = {}
        for i in range(len(s)):
            if s[i] in tlist:
                if s[i] in smap.keys():
                    smap[s[i]] += [i]
                else:
                    smap[s[i]] = [i]
        tmap = {}
        for i in range(len(t)):
            if t[i] in tmap.keys():
                tmap[t[i]] += [i]
            else:
                tmap[t[i]] = [i]
        for key in tmap.keys():
            if key in smap.keys():
                if len(smap[key]) < len(tmap[key]):
                    return ""
            else:
                return ""
        combines =[]
        combine = []
        self.combination(smap, t, combine, combines, 0)

        shortest = len(s)
        low = 0
        high = len(s) - 1
        for i in range(len(combines)):
            lenth = abs(max(combines[i]) - min(combines[i])) + 1
            if lenth < shortest:
                shortest = lenth
                low = min(combines[i])
                high = max(combines[i])
        return s[low : high + 1]
    
    def combination(self, smap, t, combine, combines, index):
        if index == len(t):
            combines.append(combine.copy())
            return
        for i in range(len(smap[t[index]])):
            val = smap[t[index]][i]
            smap[t[index]].remove(smap[t[index]][i])
            combine.append(val)
            self.combination(smap, t, combine, combines, index + 1)
            combine.pop()
            smap[t[index]].insert(i, val)

from math import inf
class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        if (len(s) < len(t)):
            return ""

        org = dict()

        for val in t:
            org[val] = 1 + org.get(val, 0)
        
        hmap = dict()
        l, r = 0, 0

        def isValid(hmap):
            cnt = 0

            for i, j in hmap.items():
                if i in org and j >= org[i]:
                    cnt += 1

            if (cnt != len(org)):
                return False

            return True

        min_val = inf
        start, end = -1, -1

        for r, r_val in enumerate(s):

            hmap[r_val] = 1 + hmap.get(r_val, 0)

            while (l <= r and isValid(hmap)):

                if min_val > r - l + 1:
                    min_val = r - l + 1
                    start, end = l, r + 1

                hmap[s[l]] -= 1
                l += 1

        return s[start : end]
    
solution = Solution()

s = "ADOBECODEBANC"
t = "ABC"#"BANC"
print(solution.minWindow(s, t))

s = "a"
t = "a"
print(solution.minWindow(s, t))

s = "a"
t = "aa"
print(solution.minWindow(s, t))

s = "a"
t = "b"
print(solution.minWindow(s, t))

s = "aa"
t = "aa"
print(solution.minWindow(s, t))