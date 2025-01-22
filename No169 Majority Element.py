from collections import Counter
class Solution:
    def majorityElement(self, nums):
        freq = Counter(nums)

        for key in freq.keys():
            if freq[key] > len(nums)/2:
                return key  
        return None

solution = Solution()

nums = [3,2,3]
print(solution.majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(solution.majorityElement(nums))

