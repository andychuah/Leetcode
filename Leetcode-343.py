class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n-1
        else:
            div, rem = n/3, n%3
            if rem == 0:
                return pow(3,div)
            elif rem == 1:
                div = div - 1
                rem = rem + 3
                return pow(3,div) * rem
            elif rem == 2:
                return pow(3,div) * rem