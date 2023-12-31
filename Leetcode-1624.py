class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        first_index = {}
        res = -1

        for i in range(len(s)):
            if s[i] in first_index:
                res = max(res, i - first_index[s[i]] - 1)
            else:
                first_index[s[i]] = i
        return res

