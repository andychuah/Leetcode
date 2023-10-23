import math
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0 or n == 0:
            return False
        print(math.log(n) % math.log(4))
        if n == 1 or math.log(n) / math.log(4) == int(math.log(n) / math.log(4)):
            return True
        else:
            return False
        