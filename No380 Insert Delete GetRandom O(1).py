from collections import defaultdict
import random

class RandomizedSet:

    def __init__(self):
        self.indmap = defaultdict(int) # store the map of numbers and lists
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.indmap:
            return False
        self.nums.append(val)
        self.indmap[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        # this is tricky. to reach O(1), we replace the number in the middle of list with the number on the end of list and pop the end
        if not val in self.indmap:
            return False
        index = self.indmap[val]
        self.nums[index] = self.nums[-1]
        self.indmap[self.nums[-1]] = index
        self.nums.pop()
        self.indmap.pop(val)
        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self.nums) - 1)
        return self.nums[index]
        

randomizedSet = RandomizedSet()
randomizedSet.insert(1) # Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2) # Returns false as 2 does not exist in the set.
randomizedSet.insert(2) # Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom() # getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1) # Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2) # 2 was already in the set, so return false.
randomizedSet.getRandom() # Since 2 is the only number in the set, getRandom() will always return 2.