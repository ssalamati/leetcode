class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        res = 0
        for price in prices:
            if price > m:
                res = max(res, price - m)
            else:
                m = price

        return res
