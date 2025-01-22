from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        freq = [[n, c] for c, n in count.items()]
        freq.sort(reverse = True)
        result = ""
        for n, c in freq:
            result += c * n
        return result

solution = Solution()
print(solution.frequencySort("tree"))
print(solution.frequencySort("cccaaa"))
print(solution.frequencySort("Aabb"))