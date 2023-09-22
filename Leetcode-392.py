class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in s:
            if i in t:
                tIndex = t.index(i)
                if len(t) > 0:
                    t = t[tIndex+1:]
                continue
            else:
                return False
        return True
        