class Solution:
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])
        inserintervals = []
        inserintervals.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] > inserintervals[-1][1]:
                inserintervals.append(intervals[i])
            elif intervals[i][1] > inserintervals[-1][1]:
                inserintervals[-1][1] = intervals[i][1]
        return inserintervals

intervals = [[1,3],[6,9]]
newInterval = [2,5]
solution = Solution()
print(solution.insert(intervals, newInterval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(solution.insert(intervals, newInterval))