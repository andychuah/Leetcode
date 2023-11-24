class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        res = 0
        n = len(piles)

        for i in range( n // 3, n, 2):
            res += piles[i]
        
        return res