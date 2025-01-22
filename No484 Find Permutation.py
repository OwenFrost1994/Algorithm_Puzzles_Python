# 这个可以用一个stack存从小到大的数字，然后往里面填充，其实也可以直接对数字换顺序
# 道理其实比较简单，他遇到N个D就选择一组最小的从小到大的值倒序放进去，遇到I就加一个最小值
# 对n=2, 我们有一个list[1,2]对应I，[2,1]对应D
# 对n=3, 我们有一个list[1,2,3]对应II，[2,1,3]对应DI,[1,3,2]对应ID,[3,2,1]对应DD
from typing import List

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        result = list(range(1, len(s) + 2))
        i = 0
        j = 0
        while j < len(s):
            while j < len(s) and s[j] == "D":
                j += 1
            result[i:j + 1] = result[i:j + 1][::-1]
            j += 1
            i = j
        return result

solution = Solution()
print(solution.findPermutation(s = "I"))
print(solution.findPermutation(s = "D"))
print(solution.findPermutation(s = "DI"))
print(solution.findPermutation(s = "ID"))
print(solution.findPermutation(s = "III"))
print(solution.findPermutation(s = "DDI"))
print(solution.findPermutation(s = "IDI"))
print(solution.findPermutation(s = "IDD"))