from collections import deque
class NestedIterator:
    def __init__(self, nestedList):
        self.stack = deque()
        self.stackload(nestedList)
    
    def next(self) -> int:
        if self.hasNext():
            return self.stack.popleft().getInteger()
        else:
            return None
    
    def hasNext(self) -> bool:
        while self.stack and not self.stack[0].isInteger():
            ls = self.stack.popleft().getList()
            self.stackload(ls)
        return bool(self.stack)

    def stackload(self, nestedList):
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.appendleft(nestedList[i])