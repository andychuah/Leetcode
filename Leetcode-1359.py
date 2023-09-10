class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        else:
            return (n*(2*n-1)*self.countOrders(n-1))%(10**9+7)