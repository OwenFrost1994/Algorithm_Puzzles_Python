class Solution:
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        while j < n:
            if i < m:
                if nums1[i] <= nums2[j]:
                    i += 1
                else:
                    k = m
                    while(k > i):
                        nums1[k] = nums1[k - 1]
                        k -= 1
                    nums1[i] = nums2[j]
                    j += 1
                    m += 1
            else:
                nums1[i] = nums2[j]
                i += 1
                j += 1
        return nums1
        """
        Do not return anything, modify nums1 in-place instead.
        """
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution = Solution()
print(solution.merge(nums1, m , nums2, n))

nums1 = [1]
m = 1
nums2 = []
n = 0
print(solution.merge(nums1, m , nums2, n))

nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(solution.merge(nums1, m , nums2, n))