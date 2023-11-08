class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        """
        :type sx: int
        :type sy: int
        :type fx: int
        :type fy: int
        :type t: int
        :rtype: bool
        """
        if sx == fx and sy == fy:
            return t != 1
        maxDistance = max(abs(sx - fx), abs(sy - fy))
        return maxDistance <= t