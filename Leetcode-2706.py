class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        # Time: O(n) - 36ms
        minPrice, secondMinPrice = min(prices[0], prices[1]), max(prices[0], prices[1])
        for i in range(2, len(prices)):
            if prices[i] < minPrice:
                secondMinPrice = minPrice
                minPrice = prices[i]
            elif prices[i] < secondMinPrice:
                secondMinPrice = prices[i]
        cheapestChoc = minPrice + secondMinPrice
        return money if cheapestChoc > money else money-cheapestChoc


        '''
        Time: O(nlogn) - 46ms
        prices.sort()
        cheapestChoc = prices[0] + prices[1]
        return money if cheapestChoc > money else money-cheapestChoc
        '''