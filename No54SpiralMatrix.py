class Solution(object):
    entrylist = []
    def spiralOrder(self, matrix):
        self.entrylist = []
        self.spiral(matrix)
        return self.entrylist

    def spiral(self, matrix):
        if len(matrix) == 0:
            return
        self.entrylist.extend(matrix[0])
        matrix.remove(matrix[0])
        for i in range(len(matrix)):
            self.entrylist.append(matrix[i][len(matrix[i])-1])
            matrix[i].remove(matrix[i][len(matrix[i])-1])
        if len(matrix) > 0:
            self.entrylist.extend(list(reversed(matrix[len(matrix)-1])))
            matrix.remove(matrix[len(matrix)-1])
        for i in range(len(matrix)-1, -1, -1):
            self.entrylist.append(matrix[i][0])
            matrix[i].remove(matrix[i][0])
        self.spiral(matrix)


solution = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(solution.spiralOrder(matrix))
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(solution.spiralOrder(matrix))