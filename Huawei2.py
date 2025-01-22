import bisect
class numstem():
    def __init__(self) -> None:
        self.nums = []
        self.len = 0
        self.medium = 0
    
    def add(self, num):
        if self.len == 0:
            self.nums.append(num)
            self.medium = num
            self.len = 1
            return True
        index = bisect.bisect_left(self.nums, num)
        if index < self.len:
            self.nums.insert(index, num)
            self.len += 1
        else:
            self.nums.append(num)
            self.len += 1
        if self.len % 2 != 0:
            self.medium = self.nums[self.len//2]
        else:
            self.medium = (self.nums[self.len//2] + self.nums[self.len//2 - 1])/2
    
    def get_medium(self):
        return self.medium

NUMSTEM = numstem()
NUMSTEM.add(1)
print(NUMSTEM.get_medium())
NUMSTEM.add(3)
print(NUMSTEM.get_medium())
NUMSTEM.add(2)
print(NUMSTEM.get_medium())
NUMSTEM.add(6)
print(NUMSTEM.get_medium())
NUMSTEM.add(5)
print(NUMSTEM.get_medium())