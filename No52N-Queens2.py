class Solution(object):
    numresult = 0
    def totalNQueens(self, n):
        Array = [0]*n
        self.numresult = 0
        self.solve(Array, n , 0)
        return self.numresult

    def solve(self, Array, n, index):
        if index == n:
            self.numresult += 1
            return
        for i in range(n):
            Array[index] = i
            if self.allow(Array, index):
                self.solve(Array, n, index + 1)
            Array[index] = 0

    def allow(self, Array, index):
        for i in range(index):
            if Array[i] == Array[index] or abs(index-i) == abs(Array[index]-Array[i]):
                return False
        return True

n = 4
solution = Solution()
print(solution.totalNQueens(n))