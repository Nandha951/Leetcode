from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2])) # 4
# print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9
# print(sol.longestConsecutive([1,2,0,1])) # 3