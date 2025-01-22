class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        preorder = preorder.split(",")
        for num in preorder:
            stack.append(num)
            while len(stack) >= 3 and stack[-1] == "#" and stack[-2] == "#" and stack[-3] != "#":
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append("#")
        if len(stack) == 1 and stack[-1] == "#":
            return True
        return False

solution = Solution()
print(solution.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
print(solution.isValidSerialization("1,#"))
print(solution.isValidSerialization("1,#"))