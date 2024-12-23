class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []

        arr_with_indices = [(num, i) for i, num in enumerate(nums)]
        arr_with_indices.sort()

        left, right = 0, len(arr_with_indices) - 1
        while left < right:
            current_sum = arr_with_indices[left][0] + arr_with_indices[right][0]
            if current_sum == target:
                return [arr_with_indices[left][1], arr_with_indices[right][1]]
            elif current_sum < target:
                left+=1
            elif current_sum > target:
                right-=1