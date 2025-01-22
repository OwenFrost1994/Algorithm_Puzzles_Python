from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        result = defaultdict(list)

        for str in strs:
            str_sort = ''.join(sorted(str))
            result[str_sort].append(str)
        return list(result.values())

strs = ["eat","tea","tan","ate","nat","bat"]
solution = Solution()
print(solution.groupAnagrams(strs))