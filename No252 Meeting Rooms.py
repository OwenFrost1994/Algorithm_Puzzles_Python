# from itertools import pairwise
# class Solution:
#     def canAttendMeetings(self, intervals) -> bool:
#         intervals.sort(key=lambda x: x[0])
#         return not any(a[1] > b[0] for a,b in pairwise(intervals))
class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort()
        n = len(intervals)
        for i in range(n-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
    
solution = Solution()
print(solution.canAttendMeetings([[0,30],[5,10],[15,20]]))

print(solution.canAttendMeetings([[7,10],[2,4]]))
