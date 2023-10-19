class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i , j = 0, 0
        while i < len(s):
            if s[i] == '#' and i != 0:
                s = s[0:i-1] + s[i+1:]
                i -= 1
            elif s[i] == '#' and i == 0:
                s = s[1:]
            else:
                i += 1
        while j < len(t):
            if t[j] == '#' and j != 0:
                t = t[0:j-1] + t[j+1:]
                j -= 1
            elif t[j] == '#' and j == 0:
                t = t[1:]
            else:
                j += 1
        return True if s == t else False
        