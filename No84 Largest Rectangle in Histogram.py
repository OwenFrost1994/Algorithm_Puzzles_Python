class Solution:
    def largestRectangleArea(self, heights) -> int:
        maxArea = 0
        stack = [] # startIdx, height
        heights.append(0) # allows us to clear out stack without extra logic
        for curI, curH in enumerate(heights):
            # don't need to append if we already have the value with a lower startIdx
            if stack and curH == stack[-1][1]:
                continue
            minStartIdx = curI
            while stack and curH < stack[-1][1]:
                startIdx, lastHeight = stack.pop()
                minStartIdx = startIdx
                maxArea = max(maxArea, lastHeight * (curI - startIdx))
            stack.append((minStartIdx, curH))
        return maxArea

solution = Solution()

heights = [2,1,5,6,2,3]
print(solution.largestRectangleArea(heights))

heights = [2,4]
print(solution.largestRectangleArea(heights))