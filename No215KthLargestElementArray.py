import heapq
class Solution:
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,num)
        return heap[0]

nums = [3,2,1,5,6,4]
k = 2
solution = Solution()
print(solution.findKthLargest(nums, k))

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(solution.findKthLargest(nums, k))

nums = [2,1]
k = 2
print(solution.findKthLargest(nums, k))