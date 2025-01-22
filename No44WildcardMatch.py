class Solution(object):
    def isMatch(self, s, p):
        slen = len(s)
        plen = len(p)
        sind, pind = 0, 0
        ps, sback = -1, -1
        while (sind < slen):
            if pind < plen and p[pind] in ['?', s[sind]]:
                pind += 1
                sind += 1
            elif pind < plen and p[pind] == '*':
                ps = pind
                sback = sind
                pind += 1
            else:
                if ps == -1:
                    return False
                else :
                    pind = ps + 1
                    sind = sback + 1
                    sback = sind
        return all(p[idx] == '*' for idx in range(pind, plen))

solution = Solution()
print(solution.isMatch("aa", "a"))
print(solution.isMatch("aa", "*"))
print(solution.isMatch("cb", "?a"))