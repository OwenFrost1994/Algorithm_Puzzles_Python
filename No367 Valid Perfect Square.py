class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        for i in range(num // 2 + 1):
            if i ** 2 == num:
                return True
        return False
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            mid  = left + (right - left) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
solution = Solution()
print(solution.isPerfectSquare(1))
print(solution.isPerfectSquare(4))
print(solution.isPerfectSquare(16))
print(solution.isPerfectSquare(14))
print(solution.isPerfectSquare(25))
print(solution.isPerfectSquare(27))
print(solution.isPerfectSquare(36))