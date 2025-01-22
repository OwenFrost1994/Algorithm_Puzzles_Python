class Solution:
    def nthSuperUglyNumber(self, n: int, primes) -> int:
        size = len(primes)
        ugly = 1
        dp = [1]
        index = [0]*size
        uglynums = [1]*size
        for i in range(1, n):
            for j in range(0, size):
                if uglynums[j] == ugly:
                    uglynums[j] = dp[index[j]] * primes[j]
                    index[j] += 1
            ugly = min(uglynums)
            dp.append(ugly)
        return dp[-1]
    
import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes) -> int:
        nums = primes.copy() # do a deep copy 
        heapq.heapify(nums) #create a heap
        p = 1
        for i in range(n - 1):
            p = heapq.heappop(nums) #take the smallest element
            for prime in primes:
                heapq.heappush(nums, p * prime) #add all those multiples with the smallest number
                if p % prime == 0:
                    break
        return p
solution = Solution()
print(solution.nthSuperUglyNumber(n = 12, primes = [2,7,13,19]))
print(solution.nthSuperUglyNumber(n = 1, primes = [2,3,5]))