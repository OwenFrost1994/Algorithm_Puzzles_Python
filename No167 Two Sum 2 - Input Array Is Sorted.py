class Solution:
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            second  = target - numbers[i]
            if second in numbers[i + 1:]:
                print(numbers[i + 1:].index(second))
                return [i + 1, numbers[i + 1:].index(second) + i + 2]
        return []

solution = Solution()

numbers = [0,0,3,4]
target = 0
print(solution.twoSum(numbers, target))

numbers = [2,7,11,15]
target = 9
print(solution.twoSum(numbers, target))

numbers = [2,3,4]
target = 6
print(solution.twoSum(numbers, target))

numbers = [-1,0]
target = -1
print(solution.twoSum(numbers, target))