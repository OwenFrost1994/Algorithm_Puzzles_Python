class Solution:
    def minMeetingRooms(self, intervals):
        if len(intervals) == 0:
            return 0
        intervals.sort()
        n = len(intervals)
        results  = [[intervals.pop(0)]]
        while intervals:
            lenth = len(results)
            interval = intervals.pop(0)
            f = 0
            for i in range(lenth):
                if results[i][-1][1] <= interval[0]:
                    results[i].append(interval)
                    f = 1
                    break
            if f == 0:
                results.append([interval])
        return len(results)
solution = Solution()
print(solution.minMeetingRooms([[0,30],[5,10],[15,20]]))

print(solution.minMeetingRooms([[7,10],[2,4]]))