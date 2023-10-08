class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        min_price = prices[0]

        for price in prices[1:] :
            maxProfit = max(maxProfit, price - min_price)
            min_price = min(min_price, price)
        return maxProfit