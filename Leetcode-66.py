class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit = int(''.join(map(str,digits)))
        return list(map(int, str(digit+1)))