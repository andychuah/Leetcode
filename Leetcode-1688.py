class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        match = 0
        while n != 1:
            match += n // 2
            n -= n // 2
        return match
