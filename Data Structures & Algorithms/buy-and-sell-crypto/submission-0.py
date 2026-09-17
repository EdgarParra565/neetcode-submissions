class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 101
        max_price = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_price = max(max_price, prices[i] - min_price)
        if max_price < 0:
            return 0
        else:
            return max_price
        