from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l < r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return letters[0] if letters[l] <= target else letters[l]

solution = Solution()
print(solution.nextGreatestLetter(letters = ["c","f","j"], target = "a"))
print(solution.nextGreatestLetter(letters = ["c","f","j"], target = "c"))
print(solution.nextGreatestLetter(letters = ["x","x","y","y"], target = "z"))