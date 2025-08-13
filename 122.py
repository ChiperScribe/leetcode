class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 음수를 제외하고 덧셈을 하는 방법 - sum(max(a, 0))
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
