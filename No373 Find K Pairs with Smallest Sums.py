from typing import List
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []; res = []
        for i in range(min(len(nums1), k)):
            tup = [nums1[i], nums2[0]]
            heapq.heappush(h, [sum(tup), tup, 0])
        while k>0 and len(h)>0:
            v = heapq.heappop(h)
            res.append(v[1])
            ind = v[2] + 1
            if ind != len(nums2):
                tup = [v[1][0], nums2[ind]]
                heapq.heappush(h, [sum(tup), tup, ind])
            k -= 1
        return res
class Solution1:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []; result = []
        for i in range(len(nums2)):
            heapq.heappush(h, [nums1[0] + nums2[i], [nums1[0], nums2[i]], 0]) # sum of turple, the real turple, the index of entry in nums1
        n = 0
        while n < k and h:
            entry = heapq.heappop(h)
            result.append(entry[1]) # append the tuple with smallest sum
            index = entry[2] + 1 # use the entry in nums1 and increase by 1
            if index < len(nums1):
                heapq.heappush(h, [nums1[index] + entry[1][1], [nums1[index], entry[1][1]], index])
            n += 1
        return result
    
solution = Solution()
print(solution.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 5))
print(solution.kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 5))
print(solution.kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 3))
print(solution.kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 4))