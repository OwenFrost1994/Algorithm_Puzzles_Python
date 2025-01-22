from collections import defaultdict
import random

class RandomizedCollection:

    def __init__(self):
        self.indmap = defaultdict(set) # store the map of numbers and lists
        self.nums = []

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.indmap[val].add(len(self.nums) - 1)
        return len(self.indmap[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.indmap[val]:
            return False
        remove_index, last_val = self.indmap[val].pop(), self.nums[-1]
        self.nums[remove_index] = last_val
        self.indmap[last_val].add(remove_index)
        self.indmap[last_val].discard(len(self.nums) - 1)
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self.nums) - 1)
        return self.nums[index]

# randomizedCollection = RandomizedCollection()
# randomizedCollection.insert(1) # return true since the collection does not contain 1.
#  # Inserts 1 into the collection.
# randomizedCollection.insert(1) # return false since the collection contains 1.
#  # Inserts another 1 into the collection. Collection now contains [1,1].
# randomizedCollection.insert(2) # return true since the collection does not contain 2.
#  # Inserts 2 into the collection. Collection now contains [1,1,2].
# randomizedCollection.getRandom() # getRandom should:
#  # - return 1 with probability 2/3, or
#  # - return 2 with probability 1/3.
# randomizedCollection.remove(1) # return true since the collection contains 1.
#  # Removes 1 from the collection. Collection now contains [1,2].
# randomizedCollection.getRandom() # getRandom should return 1 or 2, both equally likely.

randomizedCollection = RandomizedCollection()
randomizedCollection.insert(1)
randomizedCollection.remove(1)
randomizedCollection.insert(1)