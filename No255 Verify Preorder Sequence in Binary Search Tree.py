class Solution:
    def verifyPreorder(self, preorder) -> bool:
        if len(preorder) <= 1:
            return True
        stack = []
        last = -1000000
        for n in preorder:
            if n < last:
                return False
            while stack and n > stack[-1]:
                last = stack.pop()
            stack.append(n)
        return True
solution = Solution()
print(solution.verifyPreorder([5,3,1,2,6]))
print(solution.verifyPreorder([5,2,1,3,6]))
print(solution.verifyPreorder([5,2,6,1,3]))
