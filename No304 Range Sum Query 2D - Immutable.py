from itertools import accumulate
class NumMatrix:

    def __init__(self, matrix):
        self.sum = []
        self.sum.append([0]*(len(matrix[0])+1))
        for i in range(len(matrix)):
            num = [0]+list(accumulate(matrix[i]))
            self.sum.append([self.sum[-1][i]+num[i] for i in range(len(matrix[i])+1)])
        print(self.sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        bottomRight = self.sum[row2][col2]
        above = self.sum[row1 - 1][col2]
        left = self.sum[row2][col1 - 1]
        topLeft = self.sum[row1 - 1][col1 - 1]

        return bottomRight - above - left + topLeft
    
numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
numMatrix.sumRegion(2, 1, 4, 3)
numMatrix.sumRegion(1, 1, 2, 2)
numMatrix.sumRegion(1, 2, 2, 4)