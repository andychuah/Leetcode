class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        res = 0
        for i in left:
            res = max(res, abs(0-i))
        
        for i in right:
            res = max(res, abs(n-i))
        
        return res
        