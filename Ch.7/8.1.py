from typing import List
class Solution:
    def trap(self, heigth: List[int]) -> int:
        if not heigth:
            return 0

        volume = 0
        left, right = 0, len(heigth) - 1
        left_max, right_max = heigth[left], heigth[right]

        while left < right:
            left_max, right_max = (max(heigth[left], left_max),
                                   max(heigth[right], right_max))

            if left_max <= right_max:
                volume += left_max - heigth[left]
                left += 1
            else:
                volume += right_max - heigth[right]
                right -= 1
        return volume