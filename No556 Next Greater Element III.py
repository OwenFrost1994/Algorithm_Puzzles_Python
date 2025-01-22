# 把数转为str处理
# 找一个从低位到高位往前上升停止的地方，因为数字在str化了以后低位在n-1所以要从n-1开始
# 之后找到>i最大值也就是j的位置，交换i和j，但是这保证了比原数大，却不是在位一样的情况下最小的最大值，需要把i+1:的位反过来排序
# 835721 -> 835(i)721 -> 835(i)7(j)21 -> 837(i)5(j)21 -> 837125
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        n = len(s)
        i, j = n - 2, n - 1
        while i >= 0 and s[i] >= s[i+1]:
            i -= 1
        if i < 0:
            return -1
        while s[i] >= s[j]:
            j -= 1
        s[i], s[j] = s[j], s[i]
        s[i + 1 :] = s[i + 1 :][::-1]
        result = int(''.join(s))
        return -1 if result > 2**31 - 1 else result

solution = Solution()
print(solution.nextGreaterElement(12443322))
print(solution.nextGreaterElement(2147483486)) #overflow
print(solution.nextGreaterElement(1324))
print(solution.nextGreaterElement(12))
print(solution.nextGreaterElement(21))