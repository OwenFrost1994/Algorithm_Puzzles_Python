class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.que = [0]*k
        self.front = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.isEmpty():
            self.front = (self.front - 1 + self.capacity) % self.capacity
        self.que[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        idx = (self.front + self.size) % self.capacity
        self.que[idx] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.que[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        idx = (self.front + self.size - 1) % self.capacity
        return self.que[idx]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        if self.capacity == self.size:
            return True
        return False
        
myCircularDeque = MyCircularDeque(3)
myCircularDeque.insertLast(1) # return True
myCircularDeque.insertLast(2) # return True
myCircularDeque.insertFront(3) # return True
myCircularDeque.insertFront(4) # return False, the queue is full.
myCircularDeque.getRear() # return 2
myCircularDeque.isFull() # return True
myCircularDeque.deleteLast() #  return True
myCircularDeque.insertFront(4) # return True
myCircularDeque.getFront() # return 4