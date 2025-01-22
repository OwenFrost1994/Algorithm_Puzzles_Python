# 3->2->1 3->4->2->1 -1 is better
# 7->6->3->2->1 7->8->4->2->1 no difference
# 9->8->4->2->1 
# 11->12->6->3->2->1
# 13->12->6->3->2->1
# 15->16->8->4->2->1
# for num >= 7 any number % 4 == 3 should be +1 and the operations will be fewer
class Solution:
    def integerReplacement(self, n: int) -> int:
        result = 0
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            elif n % 4 == 3 and n > 3:
                n += 1
            else:
                n -= 1
            result += 1
        return result

solution = Solution()
print(solution.integerReplacement(1))
print(solution.integerReplacement(7))
print(solution.integerReplacement(8))
print(solution.integerReplacement(9))
print(solution.integerReplacement(11))
print(solution.integerReplacement(13))
print(solution.integerReplacement(15))