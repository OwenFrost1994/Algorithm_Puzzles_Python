from typing import List
import heapq
# sorting method
# 153ms Beats 83.05%of users with Python3 21.08MB Beats 41.31%of users with Python3
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flatten = []
        for i in range(len(matrix)):
            flatten += matrix[i]
        flatten.sort()
        return flatten[k - 1]
# use heap method
# transfer every row into a heap, and transfer total matrix into a heap with head entry of the row works as the sorting target
# heap(heap(matrix[0]), heap(matrix[1], ...))
# 203ms Beats 12.27%of users with Python3 20.76MB Beats 98.06%of users with Python3
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        for i in range(len(matrix)):
            heapq.heapify(matrix[i])
        heapq.heapify(matrix)
        result = 0
        while k:
            result = matrix[0][0]
            heapq.heappop(matrix[0])
            if not matrix[0]:
                heapq.heappop(matrix)
            if len(matrix):
                headnode = heapq.heappop(matrix)
                heapq.heappush(matrix, headnode)
            k -= 1
        return result
solution = Solution()
print(solution.kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))
print(solution.kthSmallest(matrix = [[-5]], k = 1))