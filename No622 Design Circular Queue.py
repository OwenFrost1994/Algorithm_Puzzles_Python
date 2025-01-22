class MyCircularQueue:

    def __init__(self, k: int):
        self.que = [0]*k
        self.front = 0
        self.size = 0
        self.n = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.que[(self.front + self.size) % self.n] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.n
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.que[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.que[(self.front + self.size - 1) % self.n]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.n
        
    

obj = MyCircularQueue(3)
print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.enQueue(3))
print(obj.enQueue(4))
print(obj.Rear())     # return 3
print(obj.isFull())   # return True
print(obj.deQueue())  # return True
print(obj.enQueue(4)) # return True
print(obj.Rear())     # return 4
