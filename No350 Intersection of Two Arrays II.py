class Solution:
    def intersect(self, nums1, nums2):
          nums1.sort()
          nums2.sort()
          i, j = 0, 0
          n, m = len(nums1), len(nums2)
          result = []
          while i < n and j < m:
                if nums1[i] == nums2[j]:
                    result.append(nums1[i])
                    i += 1
                    j += 1
                else:
                    if nums1[i] < nums2[j]:
                         i += 1
                    else:
                         j += 1
          return result

solution = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(solution.intersect(nums1, nums2))

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(solution.intersect(nums1, nums2))