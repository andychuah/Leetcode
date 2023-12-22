class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(1, len(s)):
            leftString, rightString = s[:i], s[i:]
            currRes = leftString.count("0") + rightString.count("1")
            if currRes == len(s):
                return currRes
            res = max(res, currRes)
        return res
        