class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        splitList = s.strip().split()
        splitList.reverse()
        return ' '.join(splitList)
        