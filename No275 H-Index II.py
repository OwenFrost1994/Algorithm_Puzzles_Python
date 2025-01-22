class Solution:
    def hIndex(self, citations) -> int:
        n = len(citations)
        s=0
        e=n-1
        while s<=e:
            mid = s+(e-s)//2
            if citations[mid] < n-mid:
                s = mid+1
            else:
                e = mid-1
        return n-s
        

solution = Solution()

citations = [0,1,3,5,6]
print(solution.hIndex(citations))

citations = [1,2,100]
print(solution.hIndex(citations))