import heapq
import collections
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        
        counts = collections.Counter(s)
        
        pq = []
        for ch, count in counts.items():
            heapq.heappush(pq, (-count, ch))

        result = []
        while pq:
            tmp = []
            d = min(k, len(s))
            for i in range(d):
                if not pq:
                    return ""
                count, ch = heapq.heappop(pq)
                result.append(ch)
                if count < -1: # pushed in as negated, so it's: if actual-positive-count > 1
                    tmp.append((count+1, ch))
                s = s[1:] # shorten s
            for count, ch in tmp:
                heapq.heappush(pq, (count, ch)) #push the unused charactors back
        return "".join(result)
    
solution = Solution()
print(solution.rearrangeString(s = "aabbcc", k = 3))
print(solution.rearrangeString(s = "aaabc", k = 3))
print(solution.rearrangeString(s = "aaadbbcc", k = 2))