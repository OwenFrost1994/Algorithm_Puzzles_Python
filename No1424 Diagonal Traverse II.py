from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        n = max([len(nums[i]) for i in range(m)])
        results = []
        for k in range(m + n - 1):
            temp = []
            if k < m:
                x = k
                y = 0
            else:
                x = m - 1
                y = k - m + 1
            while x >= 0:
                if y < len(nums[x]):
                    temp.append(nums[x][y])
                x -= 1
                y += 1
            results.extend(temp)
        return results
    
# 这个算法厉害在他直接变成一个排序问题了，排序来解决按照对角线遍历问题，再取值
# 借助python自己的排序器和迭代器,速度很快
class Solution1:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        arr = []
        for i, row in enumerate(nums):
            for j, v in enumerate(row):
                arr.append((i + j, j, v))
        arr.sort()
        return [v[2] for v in arr]
solution = Solution1()
print(solution.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(solution.findDiagonalOrder(nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))
print(solution.findDiagonalOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))