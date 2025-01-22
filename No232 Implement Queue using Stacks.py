class MyQueue:

    def __init__(self):
        self.inlist = []
        self.outlist = []

    def push(self, x: int) -> None:
        self.inlist.append(x)

    def pop(self) -> int:
        self.peek()
        return self.outlist.pop()

    def peek(self) -> int:
        if not self.outlist:
            while self.inlist:
                self.outlist.append(self.inlist.pop())
        return self.outlist[-1]

    def empty(self) -> bool:
        return not self.inlist and not self.outlist
    
myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
myQueue.peek()
myQueue.pop()
myQueue.empty()