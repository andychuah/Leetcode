class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Binary search, Runtime: 25ms
        start, end = 1, x
        while(start <= end):
            mid = start + (end - start) / 2
            if(mid * mid > x):
                end = mid - 1
            elif (mid * mid == x):
                return mid
            else:
                start = mid + 1
        return end

        '''
        Runtime : 10ms
        return int(x ** 0.5)
        '''