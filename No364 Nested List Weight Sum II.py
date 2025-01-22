from collections import deque


class Solution:
    def depthSumInverse(self, nestedList) -> int:
        # def max_depth(nestedList):
        #     depth = 1
        #     for item in nestedList:
        #         if item.isInteger():
        #             continue
        #         depth = max(depth, max_depth(item.getList())+ 1)
        #     return depth
        # def dfs(nested, depth):
        #     result = 0
        #     for item in nested:
        #         if item.isInteger():
        #             result += depth*item.getInteger()
        #         else:
        #             result += dfs(item.getList(), depth - 1)
        #     return result
        # maxdepth = max_depth(nestedList)
        # return dfs(nestedList, maxdepth)
        total, cur_total = 0, 0
        queue = deque(nestedList)
        
        while queue:
            for _ in range(len(queue)):
                ele = queue.popleft()
                if ele.isInteger():
                    cur_total += ele.getInteger() # we dont clear current total, so every round previous depth total would be accumulated again and again.
                else:
                    queue.extend(ele.getList())      
            total += cur_total
                
        return total