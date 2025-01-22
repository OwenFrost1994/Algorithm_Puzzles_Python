class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left
        while right > left:
            right = right & (right-1)
        return right
    
class Solution1:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = right
        while right > left:
            res = right & (right-1)
            right = res
        return res

solution = Solution()

left = 5
right = 7
print(solution.rangeBitwiseAnd(left, right))

left = 0
right = 0
print(solution.rangeBitwiseAnd(left, right))

left = 1
right = 2147483647
print(solution.rangeBitwiseAnd(left, right))