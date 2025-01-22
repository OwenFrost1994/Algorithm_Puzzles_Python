class Solution(object):
    
    def solveNQueens(self, n):
        Array = [0]*n
        resultlist = []
        numresult = 0
        self.solve(Array, n , 0, resultlist, numresult)
        return resultlist

    def solve(self, Array, n, index, result, num):
        if index == n:
            result.append(self.transformresult(Array, n))
            num += 1
            return
        for i in range(n):
            Array[index] = i
            if self.allow(Array, index):
                self.solve(Array, n, index + 1, result, num)
            Array[index] = 0

    def allow(self, Array, index):
        for i in range(index):
            if Array[i] == Array[index] or abs(index-i) == abs(Array[index]-Array[i]):
                return False
        return True
    
    def transformresult(self, Array, n):
        strarray = []
        for i in range(n):
            row = []
            for j in range(n):
                if (j == Array[i]):
                    row.append("Q")
                else:
                    row.append(".")
            strarray.append("".join(row))
        return strarray


n = 4
solution = Solution()
print(solution.solveNQueens(n))