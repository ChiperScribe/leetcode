class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solve by using 'in'
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
