import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums.copy()
        self.origin = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.origin.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n):
            index = random.randint(i, n - 1)
            self.nums[i], self.nums[index] = self.nums[index], self.nums[i]
        return self.nums

solution = Solution([1, 2, 3])
solution.shuffle() # Shuffle the array [1,2,3] and return its result.
 # Any permutation of [1,2,3] must be equally likely to be returned.
 # Example: return [3, 1, 2]
solution.reset() # Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle() # Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]
