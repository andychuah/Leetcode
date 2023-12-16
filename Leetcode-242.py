class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Elapse time = 31ms, Memory = 13.66MB
        def freq(s):
            ans = [0] * 26
            for c in s:
                ans[ord(c)-ord('a')] += 1
            return ans

        return freq(s) == freq(t)

        '''
        # Elapse time = 48ms, memory = 14.6MB
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        return True if s == t else False
        '''