class Solution:
    def hIndex(self, citations) -> int:
        
        i = 0
        n = len(citations)

        if n == 1:
            if citations[0] >= 1:
                return 1
            else:
                return 0
            
        citations.sort()
        hval = citations[0]
        for i in range(len(citations)-1, -1, -1):
            if citations[i] >= n - i:
                hval = n-i
        return hval

solution = Solution()

citations = [3,0,6,1,5]
print(solution.hIndex(citations))

citations = [1,3,1]
print(solution.hIndex(citations))