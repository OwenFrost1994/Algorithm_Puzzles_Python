from collections import Counter

class Solution(object):
    def permuteUnique(self, nums):
        results = []
        counter = Counter(nums)
        def findall(result):
            if len(result) == len(nums):
                results.append(result)
                return
            for key in counter:
                if counter[key] > 0:
                    counter[key] -= 1
                    findall(result+[key])
                    counter[key] += 1
        result = []
        findall(result)
        return results

nums = [1,1,2]

solution = Solution()
print(solution.permuteUnique(nums))