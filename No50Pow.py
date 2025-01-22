class Solution(object):
    def myPow(self, x, n):
        result = self.function(x, abs(n))
        if n < 0:
            return 1/result
        return result
    
    def function(self, x, n):
        if n == 0:
            return 1
        result = self.function(x, n//2)
        result = result * result

        if n % 2 == 0:
            return result
        else:
            return result*x

solution = Solution()
x = 2.00000
n = 10
print(solution.myPow(x,n))
x = 2.10000
n = 3
print(solution.myPow(x,n))
x = 2.00000
n = -2
print(solution.myPow(x,n))