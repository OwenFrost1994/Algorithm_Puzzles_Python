class Solution(object):
    def addToArrayForm(self, num, k):
        index = len(num) - 1
        add = 0
        while(k > 0 or index >= 0):
            if index < 0:
                newdigit = [0]
                newdigit.extend(num)
                num = newdigit
                num[0] = num[0] + add + k % 10
                if num[0] >= 10:
                    num[0] = num[0] % 10
                    add = 1
                else:
                    add = 0
            else:
                num[index] = num[index] + add + k % 10
                if num[index] >= 10:
                    num[index] = num[index] % 10
                    add = 1
                else:
                    add = 0
            k = k // 10
            index -= 1

        if add == 1:
            newdigit = [0]
            newdigit.extend(num)
            num = newdigit
            num[0] = num[0] + add
        return num
            

num = [1,2,0,0]
k = 34
solution = Solution()
print(solution.addToArrayForm(num, k))

num = [2,7,4]
k = 181
print(solution.addToArrayForm(num, k))

num = [2,1,5]
k = 806
print(solution.addToArrayForm(num, k))

num = [9,9,9,9,9,9,9,9,9,9]
k = 1
print(solution.addToArrayForm(num, k))

num = [0]
k = 23
print(solution.addToArrayForm(num, k))