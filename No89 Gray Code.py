class Solution:
    def grayCode(self, n: int):
        start_list = [0, 1]
        for i in range(2, n+1):
            summand = 2**(i-1)
            start_list = start_list+[elem+summand for elem in reversed(start_list)]
        return start_list

solution = Solution()

n = 1
print(solution.grayCode(n))

n = 2
print(solution.grayCode(n))

n = 3
print(solution.grayCode(n))