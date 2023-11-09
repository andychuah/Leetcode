class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, start = 0, 0
        for i in range(len(s)):
            if s[i] != s[start]:
                subStrLen = i - start
                while(subStrLen > 0):
                    res += subStrLen
                    subStrLen -= 1
                start = i
        subStr = len(s) - start
        while(subStr > 0):
            res += subStr
            subStr -= 1
        return int(res % (math.pow(10,9)+7))
        