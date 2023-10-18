class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_alnum = ""
        for i in s:
            if i.isalnum():
                str_alnum += i
        
        finalStr = str_alnum.lower()
        if finalStr == finalStr[::-1]:
            return True
        else:
            return False
        