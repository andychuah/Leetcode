class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in string.ascii_lowercase:
            first, last = s.find(i), s.rfind(i)
            if first > -1:
                res += len(set(s[first + 1: last]))
        return res
        