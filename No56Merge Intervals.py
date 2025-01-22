class Solution:
    def merge(self, intervals) :
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key = lambda x:x[0])
        mergedinter = []
        mergedinter.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] > mergedinter[-1][1]:
                mergedinter.append(intervals[i])
            elif intervals[i][1] > mergedinter[-1][1]:
                mergedinter[-1][1] = intervals[i][1]
        return mergedinter

intervals = [[1,3],[2,6],[8,10],[15,18]]
solution = Solution()
print(solution.merge(intervals))

intervals = [[1,4],[4,5]]
print(solution.merge(intervals))