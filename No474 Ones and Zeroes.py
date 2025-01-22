# 这个能最多组成多少的问题，类似前面一个array的numbers最大能够到多少，只不过变成了三阶的问题
# 二维的array表明不超过m个0和n个1的情况下，最多能涵盖几个数字
# 在二维array[m][n]，每次加一个数占用M个0和N个1都会让后面的array的元素都加1，前后状态的联系是array[i][j]和array[i-M][j-N]
# 我们在考虑不同的binary number的时候，前面的数字可能已经让值增大了，后面加进来的只要不能让最后够到的数字更大那就不改变array的值
# 遍历的时候必然需要从后往前便利，因为需要看到占了多少个01以后增加为而不是看覆盖了哪些
# array宽度必须m+1和n+1考虑0个0和0个1
from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        count = [[s.count("0"), s.count("1")] for s in strs]
        for k in range(len(strs)):
            M, N = count[k]
            for i in range(m, M - 1, -1):
                for j in range(n, N - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - M][j - N] + 1)
        return dp[-1][-1]

solution = Solution()
print(solution.findMaxForm(strs = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3))
print(solution.findMaxForm(strs = {"10", "0", "1"}, m = 1, n = 1))
