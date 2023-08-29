class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int_sum = int(a, 2) + int(b, 2)
        binary_sum = bin(int_sum)[2:] #to remove 0b prefix that shows string is binary
        return binary_sum