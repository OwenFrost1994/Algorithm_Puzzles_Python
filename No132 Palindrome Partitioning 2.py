class Solution(object):
    def minCut(self, s):
        return self.palpart(s, 0, len(s) - 1)
    
    def palpart(self, s, i, j):
        if i > j or self.isPalind(s, i, j):
            return 0
        
        mincut = len(s)
        for k in range(i, j):
            cut = self.palpart(s, i, k) + self.palpart(s, k + 1, j) + 1
            mincut = min(cut, mincut)
        
        return mincut

    def isPalind(self, s, i, j):
        if s[i:j + 1] == "".join(reversed(s[i:j + 1])):
            return True
        else:
            return False
        
class Solution1(object):
    def minCut(self, s):
        n = len(s)
        C = [[0 for i in range(n)] for i in range(n)]
        P = [[False for i in range(n)] for i in range(n)]

        j = 0
        k = 0
        L = 0
        
        for i in range(n):
            P[i][i] = True
            C[i][i] = 0
        
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1  # Set ending index   
                if L == 2:
                    P[i][j] = (s[i] == s[j])
                else:
                    P[i][j] = ((s[i] == s[j]) and P[i + 1][j - 1])
                
                if P[i][j] == True:
                    C[i][j] = 0
                else:
                    # Make a cut at every possible
                    # # location starting from i to j,
                    # # and get the minimum cost cut.
                    C[i][j] = 100000000
                    for k in range(i, j):
                        C[i][j] = min(C[i][j], C[i][k] + C[k + 1][j] + 1)

        return C[0][n - 1]
    
solution = Solution1()
# s = "aab"
# print(solution.minCut(s))

# s = "a"
# print(solution.minCut(s))

# s = "ab"
# print(solution.minCut(s))

s = "eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj"
print(solution.minCut(s))