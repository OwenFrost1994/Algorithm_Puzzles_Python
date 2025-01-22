# S = “1221121221221121122……” the occurrences of ‘1’s or ‘2’s in each group are: 1 2 2 1 1 2 1 2 2 1 2 2
# list S从1开始，之后加2，1"2"因为一个2在算频率的时候要对应两个一样的数字，也就两个一样的2,1"2"2
# 12"2"，现在还有一个2，需要对应两个1，12"2"11
# 第一个1对应一个2, 122"1"12，第二个1对应一个1, 1221"1"21
# 然后再加两个2, 12211"2"122，
# 这个偏数学问题
class Solution:
    def magicalString(self, n: int) -> int:
        # s = [1, 2, 2]
        # i = 2
        # while len(s) < n:
        #     s = s + [3-s[-1]] * s[i]
        #     i += 1
        # return s[:n].count(1)
# 很奇怪上面的不够快
        s = [1, 2, 2]
        i = 2
        while len(s) < n:
            pre = s[-1]
            cur = 3 - pre
            s += [cur] * s[i]
            i += 1
        return s[:n].count(1)

solution = Solution()
print(solution.magicalString(6))
print(solution.magicalString(1))