from collections import Counter

class Solution:
    def majorityElement(self, nums):
        result = []
        freq = Counter(nums)

        for key in freq.keys():
            if freq[key] > len(nums)/3:
                result.append(key)
        return result

solution = Solution()

nums = [3,2,3]
print(solution.majorityElement(nums))

nums = [1]
print(solution.majorityElement(nums))

nums = [1,2]
print(solution.majorityElement(nums))
