from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m+n-1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m-=1
            else:
                nums1[last] = nums2[n-1]
                n-=1
            last -= 1
        
        while n>0:
            nums1[last] = nums2[n - 1]
            n, last = n-1, last-1
        return nums1

sol = Solution()
# print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3)) # [1,2,2,3,5,6]
# print(sol.merge([1], 1, [], 0)) # [1]
# print(sol.merge([0], 0, [1], 1)) # [1]
print(sol.merge([2,0], 1, [1], 1)) # [1,2]