## 1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Majority Vote Algorithm
        # Complexity: time O(N), space O(1)
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
