from collections import deque
class MyStack(object):

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        v = len(self.q) - 1
        i = 0
        while i < v:
            self.q.append(self.q.popleft())
            i += 1
        

    def pop(self):
        return self.q.popleft()
        

    def top(self):
        return self.q[0]
        

    def empty(self):
        return len(self.q) == 0

stack = MyStack()
print(stack.empty())