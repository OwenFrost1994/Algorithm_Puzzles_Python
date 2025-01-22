from collections import Counter
from heapq import heappop, heappush
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        freq = [[n, c] for c, n in count.items()]
        freq.sort()
        result = []
        for n, c in freq:
            result += [c] * n
        return result
    
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d={}
        for i in range(len(nums)):
            if(nums[i] in d):
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        heap=[]
        arr=[]
        for i in d:
            heappush(heap,[d[i],-i])
        while(heap):
            m,n=heappop(heap)
            for i in range(m):
                arr.append(n*(-1))
        return(arr)
    
solution = Solution()
print(solution.frequencySort([1,1,2,2,2,3]))
print(solution.frequencySort([2,3,1,3,2]))
print(solution.frequencySort([-1,1,-6,4,5,-6,1,4,1]))